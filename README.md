# stackoverflow-jobs

Simple wrapper for crawling jobs data at Stack Overflow Jobs portal.

## Basic usage

Creating a query is pretty straightforward:

```python
from stackoverflow_jobs.query import Query

q = Query()
```

All query filters are available inside `filters` module. In case you want to
add new filters, all you need to do is to append them to the `Query` object:

```python
from stackoverflow_jobs.query import Query
from stackoverflow_jobs.filters import Role, Remote, Description

q = Query() \
    + Description("Android Developer") \
    + Remote() \
    + Role([Role.Type.MOBILE])
```

After you build your query, call `execute()` to fetch the data:

```python
data = q.execute()
```

**Important note:** The library queries Stack Overflow Jobs RSS feed. This
means that you need to parse the XML afterwards.

You can also retrieve the query URL using `build_query()` method, in case you
need to:

```python
q.build_query()
>>> 'https://stackoverflow.com/jobs/feed?q=Android+Developer&r=true&dr=MobileDeveloper'
```

## Installing

`stackoverflow-jobs` is available in pypi repository:

```bash
pip install stackoverflow-jobs
```
