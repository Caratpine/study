package context_example

import (
	"context"
	"encoding/json"
	"net/http"
)

type Result struct {
	Title string
	URL string
}
type Results []Result

func Search(ctx context.Context, query string) (Results, error) {
	req, err := http.NewRequest("GET", "https://ajax.googleapis.com/ajax/services/search/web?v=1.0", nil)
	if err != nil {
		return nil, err
	}
	q := req.URL.Query()
	q.Set("q", query)

	if userIP, ok := FromContext(ctx); ok {
		q.Set("userip", userIP.String())
	}
	req.URL.RawQuery = q.Encode()
	var results Results

	err = HttpDo(ctx, req, func(resp *http.Response, err error) error {
		if err != nil {
			return err
		}
		defer resp.Body.Close()
		var data struct{
			ResponseData struct{
				Results []struct{
					TitleNoFormatting string
					URL string
				}
			}
		}
		if err := json.NewDecoder(resp.Body).Decode(&data); err != nil {
			return err
		}
		for _, res := range data.ResponseData.Results {
			results = append(results, Result{Title:res.TitleNoFormatting, URL: res.URL})
		}
		return nil
	})
	return results, err
}

func HttpDo(ctx context.Context, req *http.Request, f func(*http.Response, error) error) error {
	c := make(chan error, 1)
	req = req.WithContext(ctx)
	go func() {
		c <- f(http.DefaultClient.Do(req))
	}()
	select {
	case <-ctx.Done():
		return ctx.Err()
	case err := <-c:
		return err
	}
}