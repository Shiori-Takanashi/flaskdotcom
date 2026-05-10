1. HTMLはrouterに`requested_method`と`per_page`を渡す。
2. routerは、それらを利用して、Pagenationオブジェクトを作成。
3. Paginationオブジェクトは`render_template()`でHTMLに渡される。

```python
@bp_company.route("/")
def company_list():
    pagination = get_pagination(
        request.args.get("requested_page", 1, type=int),
        request.args.get("per_page", 10, type=int),
    )
    return render_template("pages/company.html", pagination=pagination)
```
