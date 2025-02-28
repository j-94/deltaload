---
title: Pydantic V2 Plan - Pydantic
description: Data validation using Python type hints
url: https://docs.pydantic.dev/2.0/blog/pydantic-v2/
timestamp: 2025-01-20T15:48:06.374Z
domain: docs.pydantic.dev
path: 2.0_blog_pydantic-v2
---

# Pydantic V2 Plan - Pydantic


Data validation using Python type hints


## Content

* * *

Updated late 10 Jul 2022, see [pydantic#4226](https://github.com/pydantic/pydantic/pull/4226).

* * *

I've spoken to quite a few people about pydantic V2, and mention it in passing even more.

I owe people a proper explanation of the plan for V2:

*   What we will add
*   What we will remove
*   What we will change
*   How I'm intending to go about completing it and getting it released
*   Some idea of timeframe ![Image 72: 😨](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f628.svg)

Here goes...

* * *

Enormous thanks to [Eric Jolibois](https://github.com/PrettyWood), [Laurence Watson](https://github.com/Rabscuttler), [Sebastián Ramírez](https://github.com/tiangolo), [Adrian Garcia Badaracco](https://github.com/adriangb), [Tom Hamilton Stubber](https://github.com/tomhamiltonstubber), [Zac Hatfield-Dodds](https://github.com/Zac-HD), [Tom](https://github.com/czotomo) & [Hasan Ramezani](https://github.com/hramezani) for reviewing this blog post, putting up with (and correcting) my horrible typos and making great suggestions that have made this post and Pydantic V2 materially better.

* * *

Plan & Timeframe[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#plan-timeframe "Permanent link")
----------------------------------------------------------------------------------------------------

I'm currently taking a kind of sabbatical after leaving my last job to get pydantic V2 released. Why? I ask myself that question quite often. I'm very proud of how much pydantic is used, but I'm less proud of its internals. Since it's something people seem to care about and use quite a lot (26m downloads a month, used by 72k public repos, 10k stars). I want it to be as good as possible.

While I'm on the subject of why, how and my odd sabbatical: if you work for a large company who use pydantic a lot, you might encourage the company to **sponsor me a meaningful amount**, like [Salesforce did](https://twitter.com/samuel_colvin/status/1501288247670063104) (if your organisation is not open to donations, I can also offer consulting services). This is not charity, recruitment or marketing - the argument should be about how much the company will save if pydantic is 10x faster, more stable and more powerful - it would be worth paying me 10% of that to make it happen.

Before pydantic V2 can be released, we need to release pydantic V1.10 - there are lots of changes in the main branch of pydantic contributed by the community, it's only fair to provide a release including those changes, many of them will remain unchanged for V2, the rest will act as a requirement to make sure pydantic V2 includes the capabilities they implemented.

The basic road map for me is as follows:

1.  Implement a few more features in pydantic-core, and release a first version, see [below](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#motivation-pydantic-core)
2.  Work on getting pydantic V1.10 out - basically merge all open PRs that are finished
3.  Release pydantic V1.10
4.  Delete all stale PRs which didn't make it into V1.10, apologise profusely to their authors who put their valuable time into pydantic only to have their PRs closed ![Image 73: 🙏](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f64f.svg) (and explain when and how they can rebase and recreate the PR)
5.  Rename `master` to `main`, seems like a good time to do this
6.  Change the main branch of pydantic to target V2
7.  Start tearing pydantic code apart and see how many existing tests can be made to pass
8.  Rinse, repeat
9.  Release pydantic V2 ![Image 74: 🎉](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f389.svg)

Plan is to have all this done by the end of October, definitely by the end of the year.

### Breaking Changes & Compatibility ![Image 75: 🙏](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f64f.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#breaking-changes-compatibility "Permanent link")

While we'll do our best to avoid breaking changes, some things will break.

As per the [greatest pun in modern TV history](https://youtu.be/ezAlySFluEk).

> You can't make a Tomelette without breaking some Greggs.

Where possible, if breaking changes are unavoidable, we'll try to provide warnings or errors to make sure those changes are obvious to developers.

Motivation & `pydantic-core`[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#motivation-pydantic-core "Permanent link")
--------------------------------------------------------------------------------------------------------------------------

Since pydantic's initial release, with the help of wonderful contributors [Eric Jolibois](https://github.com/PrettyWood), [Sebastián Ramírez](https://github.com/tiangolo), [David Montague](https://github.com/dmontagu) and many others, the package and its usage have grown enormously. The core logic however has remained mostly unchanged since the initial experiment. It's old, it smells, it needs to be rebuilt.

The release of version 2 is an opportunity to rebuild pydantic and correct many things that don't make sense - **to make pydantic amazing ![Image 76: 🚀](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f680.svg)** .

The core validation logic of pydantic V2 will be performed by a separate package [pydantic-core](https://github.com/pydantic/pydantic-core) which I've been building over the last few months. _pydantic-core_ is written in Rust using the excellent [pyo3](https://pyo3.rs/) library which provides rust bindings for python.

The motivation for building pydantic-core in Rust is as follows:

1.  **Performance**, see [below](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#performance)
2.  **Recursion and code separation** - with no stack and little-to-no overhead for extra function calls, Rust allows pydantic-core to be implemented as a tree of small validators which call each other, making code easier to understand and extend without harming performance
3.  **Safety and complexity** - pydantic-core is a fairly complex piece of code which has to draw distinctions between many different errors, Rust is great in situations like this, it should minimise bugs (![Image 77: 🤞](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f91e.svg)) and allow the codebase to be extended for a long time to come

Note

The python interface to pydantic shouldn't change as a result of using pydantic-core, instead pydantic will use type annotations to build a schema for pydantic-core to use.

pydantic-core is usable now, albeit with an unintuitive API, if you're interested, please give it a try.

pydantic-core provides validators for common data types, [see a list here](https://github.com/pydantic/pydantic-core/blob/main/pydantic_core/schema_types.py#L314). Other, less commonly used data types will be supported via validator functions implemented in pydantic, in Python.

See [pydantic-core#153](https://github.com/pydantic/pydantic-core/issues/153) for a summary of what needs to be completed before its first release.

Headlines[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#headlines "Permanent link")
----------------------------------------------------------------------------------------

Here are some of the biggest changes expected in V2.

### Performance ![Image 78: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#performance "Permanent link")

As a result of the move to Rust for the validation logic (and significant improvements in how validation objects are structured) pydantic V2 will be significantly faster than pydantic V1.

Looking at the pydantic-core [benchmarks](https://github.com/pydantic/pydantic-core/tree/main/tests/benchmarks) today, pydantic V2 is between 4x and 50x faster than pydantic V1.9.1.

In general, pydantic V2 is about 17x faster than V1 when validating a model containing a range of common fields.

### Strict Mode ![Image 79: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#strict-mode "Permanent link")

People have long complained about pydantic for coercing data instead of throwing an error. E.g. input to an `int` field could be `123` or the string `"123"` which would be converted to `123` While this is very useful in many scenarios (think: URL parameters, environment variables, user input), there are some situations where it's not desirable.

pydantic-core comes with "strict mode" built in. With this, only the exact data type is allowed, e.g. passing `"123"` to an `int` field would result in a validation error.

This will allow pydantic V2 to offer a `strict` switch which can be set on either a model or a field.

### Formalised Conversion Table ![Image 80: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#formalised-conversion-table "Permanent link")

As well as complaints about coercion, another legitimate complaint was inconsistency around data conversion.

In pydantic V2, the following principle will govern when data should be converted in "lax mode" (`strict=False`):

> If the input data has a SINGLE and INTUITIVE representation, in the field's type, AND no data is lost during the conversion, then the data will be converted; otherwise a validation error is raised. There is one exception to this rule: string fields - virtually all data has an intuitive representation as a string (e.g. `repr()` and `str()`), therefore a custom rule is required: only `str`, `bytes` and `bytearray` are valid as inputs to string fields.

Some examples of what that means in practice:

| Field Type | Input | Single & Intuitive R. | All Data Preserved | Result |
| --- | --- | --- | --- | --- |
| `int` | `"123"` |  |  | Convert |
| `int` | `123.0` |  |  | Convert |
| `int` | `123.1` |  |  | Error |
| `date` | `"2020-01-01"` |  |  | Convert |
| `date` | `"2020-01-01T00:00:00"` |  |  | Convert |
| `date` | `"2020-01-01T12:00:00"` |  |  | Error |
| `int` | `b"1"` |  |  | Error |

(For the last case converting `bytes` to an `int` could reasonably mean `int(bytes_data.decode())` or `int.from_bytes(b'1', 'big/little')`, hence an error)

In addition to the general rule, we'll provide a conversion table which defines exactly what data will be allowed to which field types. See [the table below](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#conversion-table) for a start on this.

### Built in JSON support ![Image 81: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#built-in-json-support "Permanent link")

pydantic-core can parse JSON directly into a model or output type, this both improves performance and avoids issue with strictness - e.g. if you have a strict model with a `datetime` field, the input must be a `datetime` object, but clearly that makes no sense when parsing JSON which has no `datatime` type. Same with `bytes` and many other types.

Pydantic V2 will therefore allow some conversion when validating JSON directly, even in strict mode (e.g. `ISO8601 string -> datetime`, `str -> bytes`) even though this would not be allowed when validating a python object.

In future direct validation of JSON will also allow:

*   parsing in a separate thread while starting validation in the main thread
*   line numbers from JSON to be included in the validation errors

(These features will not be included in V2, but instead will hopefully be added later.)

Note

Pydantic has always had special support for JSON, that is not going to change.

While in theory other formats could be specifically supported, the overheads and development time are significant and I don't think there's another format that's used widely enough to be worth specific logic. Other formats can be parsed to python then validated, similarly when serializing, data can be exported to a python object, then serialized, see [below](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#improvements-to-dumpingserializationexport).

### Validation without a Model ![Image 82: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#validation-without-a-model "Permanent link")

In pydantic V1 the core of all validation was a pydantic model, this led to a significant performance penalty and extra complexity when the output data type was not a model.

pydantic-core operates on a tree of validators with no "model" type required at the base of that tree. It can therefore validate a single `string` or `datetime` value, a `TypedDict` or a `Model` equally easily.

This feature will provide significant addition performance improvements in scenarios like:

*   Adding validation to `dataclasses`
*   Validating URL arguments, query strings, headers, etc. in FastAPI
*   Adding validation to `TypedDict`
*   Function argument validation
*   Adding validation to your custom classes, decorators...

In effect - anywhere where you don't care about a traditional model class instance.

We'll need to add standalone methods for generating JSON Schema and dumping these objects to JSON, etc.

### Required vs. Nullable Cleanup ![Image 83: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#required-vs-nullable-cleanup "Permanent link")

Pydantic previously had a somewhat confused idea about "required" vs. "nullable". This mostly resulted from my misgivings about marking a field as `Optional[int]` but requiring a value to be provided but allowing it to be `None` - I didn't like using the word "optional" in relation to a field which was not optional.

In pydantic V2, pydantic will move to match dataclasses, thus:

Required vs. Nullable

```
from pydantic import BaseModel

class Foo(BaseModel):
    f1: str  # required, cannot be None
    f2: str | None  # required, can be None - same as Optional[str] / Union[str, None]
    f3: str | None = None  # not required, can be None
    f4: str = 'Foobar'  # not required, but cannot be None
```

### Validator Function Improvements ![Image 84: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg) ![Image 85: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg) ![Image 86: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#validator-function-improvements "Permanent link")

This is one of the changes in pydantic V2 that I'm most excited about, I've been talking about something like this for a long time, see [pydantic#1984](https://github.com/pydantic/pydantic/issues/1984), but couldn't find a way to do this until now.

Fields which use a function for validation can be any of the following types:

*   **function before mode** - where the function is called before the inner validator is called
*   **function after mode** - where the function is called after the inner validator is called
*   **plain mode** - where there's no inner validator
*   **wrap mode** - where the function takes a reference to a function which calls the inner validator, and can therefore modify the input before inner validation, modify the output after inner validation, conditionally not call the inner validator or catch errors from the inner validator and return a default value, or change the error

An example how a wrap validator might look:

Wrap mode validator function

```
from datetime import datetime
from pydantic import BaseModel, ValidationError, validator

class MyModel(BaseModel):
    timestamp: datetime

    @validator('timestamp', mode='wrap')
    def validate_timestamp(cls, v, handler):
        if v == 'now':
            # we don't want to bother with further validation,
            # just return the new value
            return datetime.now()
        try:
            return handler(v)
        except ValidationError:
            # validation failed, in this case we want to
            # return a default value
            return datetime(2000, 1, 1)
```

As well as being powerful, this provides a great "escape hatch" when pydantic validation doesn't do what you need.

### More powerful alias(es) ![Image 87: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#more-powerful-aliases "Permanent link")

pydantic-core can support alias "paths" as well as simple string aliases to flatten data as it's validated.

Best demonstrated with an example:

Alias paths

```
from pydantic import BaseModel, Field

class Foo(BaseModel):
    bar: str = Field(aliases=[['baz', 2, 'qux']])

data = {
    'baz': [
        {'qux': 'a'},
        {'qux': 'b'},
        {'qux': 'c'},
        {'qux': 'd'},
    ]
}

foo = Foo(**data)
assert foo.bar == 'c'
```

`aliases` is a list of lists because multiple paths can be provided, if so they're tried in turn until a value is found.

Tagged unions will use the same logic as `aliases` meaning nested attributes can be used to select a schema to validate against.

### Improvements to Dumping/Serialization/Export ![Image 88: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg) ![Image 89: 😕](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f615.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#improvements-to-dumpingserializationexport "Permanent link")

(I haven't worked on this yet, so these ideas are only provisional)

There has long been a debate about how to handle converting data when extracting it from a model. One of the features people have long requested is the ability to convert data to JSON compliant types while converting a model to a dict.

My plan is to move data export into pydantic-core, with that, one implementation can support all export modes without compromising (and hopefully significantly improving) performance.

I see four different export/serialization scenarios:

1.  Extracting the field values of a model with no conversion, effectively `model.__dict__` but with the current filtering logic provided by `.dict()`
2.  Extracting the field values of a model recursively (effectively what `.dict()` does now) - sub-models are converted to dicts, but other fields remain unchanged.
3.  Extracting data and converting at the same time (e.g. to JSON compliant types)
4.  Serializing data straight to JSON

I think all 4 modes can be supported in a single implementation, with a kind of "3.5" mode where a python function is used to convert the data as the user wishes.

The current `include` and `exclude` logic is extremely complicated, but hopefully it won't be too hard to translate it to Rust.

We should also add support for `validate_alias` and `dump_alias` as well as the standard `alias` to allow for customising field keys.

### Validation Context ![Image 90: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#validation-context "Permanent link")

Pydantic V2 will add a new optional `context` argument to `model_validate` and `model_validate_json` which will allow you to pass information not available when creating a model to validators. See [pydantic#1549](https://github.com/pydantic/pydantic/issues/1549) for motivation.

Here's an example of `context` might be used:

Context during Validation

```
from pydantic import BaseModel, EmailStr, validator

class User(BaseModel):
    email: EmailStr
    home_country: str

    @validator('home_country')
    def check_home_country(cls, v, context):
        if v not in context['countries']:
            raise ValueError('invalid country choice')
        return v

async def add_user(post_data: bytes):
    countries = set(await db_connection.fetch_all('select code from country'))
    user = User.model_validate_json(post_data, context={'countries': countries})
    ...
```

Note

We (actually mostly Sebastián ![Image 91: 😉](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f609.svg)) will have to make some changes to FastAPI to fully leverage `context` as we'd need some kind of dependency injection to build context before validation so models can still be passed as arguments to views. I'm sure he'll be game.

Warning

Although this will make it slightly easier to run synchronous IO (HTTP requests, DB. queries, etc.) from within validators, I strongly advise you keep IO separate from validation - do it before and use context, do it afterwards, avoid where possible making queries inside validation.

### Model Namespace Cleanup ![Image 92: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#model-namespace-cleanup "Permanent link")

For years I've wanted to clean up the model namespace, see [pydantic#1001](https://github.com/pydantic/pydantic/issues/1001). This would avoid confusing gotchas when field names clash with methods on a model, it would also make it safer to add more methods to a model without risking new clashes.

After much deliberation (and even giving a lightning talk at the python language submit about alternatives, see [this discussion](https://discuss.python.org/t/better-fields-access-and-allowing-a-new-character-at-the-start-of-identifiers/14529)). I've decided to go with the simplest and clearest approach, at the expense of a bit more typing:

All methods on models will start with `model_`, fields' names will not be allowed to start with `"model"` (aliases can be used if required).

This will mean `BaseModel` will have roughly the following signature.

New BaseModel methods

```
class BaseModel:
    model_fields: List[FieldInfo]
"""previously `__fields__`, although the format will change a lot"""
    @classmethod
    def model_validate(cls, data: Any, *, context=None) -> Self:  # (1)
"""
        previously `parse_obj()`, validate data
        """
    @classmethod
    def model_validate_json(
        cls,
        data: str | bytes | bytearray,
        *,
        context=None
    ) -> Self:
"""
        previously `parse_raw(..., content_type='application/json')`
        validate data from JSON
        """
    @classmethod
    def model_is_instance(cls, data: Any, *, context=None) -> bool: # (2)
"""
        new, check if data is value for the model
        """
    @classmethod
    def model_is_instance_json(
        cls,
        data: str | bytes | bytearray,
        *,
        context=None
    ) -> bool:
"""
        Same as `model_is_instance`, but from JSON
        """
    def model_dump(
        self,
        include: ... = None,
        exclude: ... = None,
        by_alias: bool = False,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        mode: Literal['unchanged', 'dicts', 'json-compliant'] = 'unchanged',
        converter: Callable[[Any], Any] | None = None
    ) -> Any:
"""
        previously `dict()`, as before
        with new `mode` argument
        """
    def model_dump_json(self, ...) -> str:
"""
        previously `json()`, arguments as above
        effectively equivalent to `json.dump(self.model_dump(..., mode='json'))`,
        but more performant
        """
    def model_json_schema(self, ...) -> dict[str, Any]:
"""
        previously `schema()`, arguments roughly as before
        JSON schema as a dict
        """
    def model_update_forward_refs(self) -> None:
"""
        previously `update_forward_refs()`, update forward references
        """
    @classmethod
    def model_construct(
        self,
        _fields_set: set[str] | None = None,
        **values: Any
    ) -> Self:
"""
        previously `construct()`, arguments roughly as before
        construct a model with no validation
        """
    @classmethod
    def model_customize_schema(cls, schema: dict[str, Any]) -> dict[str, Any]:
"""
        new, way to customize validation,
        e.g. if you wanted to alter how the model validates certain types,
        or add validation for a specific type without custom types or
        decorated validators
        """
    class ModelConfig:
"""
        previously `Config`, configuration class for models
        """
```

1.  see [Validation Context](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#validation-context) for more information on `context`
2.  see [`is_instance` checks](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#is_instance-like-checks)

The following methods will be removed:

*   `.parse_file()` - was a mistake, should never have been in pydantic
*   `.parse_raw()` - partially replaced by `.model_validate_json()`, the other functionality was a mistake
*   `.from_orm()` - the functionality has been moved to config, see [other improvements](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#other-improvements) below
*   `.schema_json()` - mostly since it causes confusion between pydantic validation schema and JSON schema, and can be replaced with just `json.dumps(m.model_json_schema())`
*   `.copy()` instead we'll implement `__copy__` and let people use the `copy` module (this removes some functionality) from `copy()` but there are bugs and ambiguities with the functionality anyway

### Strict API & API documentation ![Image 93: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#strict-api-api-documentation "Permanent link")

When preparing for pydantic V2, we'll make a strict distinction between the public API and private functions & classes. Private objects will be clearly identified as private via a `_internal` sub package to discourage use.

The public API will have API documentation. I've recently been working with the wonderful [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings) package for both [dirty-equals](https://dirty-equals.helpmanual.io/) and [watchfiles](https://watchfiles.helpmanual.io/) documentation. I intend to use `mkdocstrings` to generate complete API documentation for V2.

This wouldn't replace the current example-based somewhat informal documentation style but instead will augment it.

### Error descriptions ![Image 94: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#error-descriptions "Permanent link")

The way line errors (the individual errors within a `ValidationError`) are built has become much more sophisticated in pydantic-core.

There's a well-defined [set of error codes and messages](https://github.com/pydantic/pydantic-core/blob/main/src/errors/kinds.rs).

More will be added when other types are validated via pure python validators in pydantic.

I would like to add a dedicated section to the documentation with extra information for each type of error.

This would be another key in a line error: `documentation`, which would link to the appropriate section in the docs.

Thus, errors might look like:

Line Errors Example

```
[
    {
        'kind': 'greater_than_equal',
        'loc': ['age'],
        'message': 'Value must be greater than or equal to 18',
        'input_value': 11,
        'context': {'ge': 18},
        'documentation': 'https://pydantic.dev/errors/#greater_than_equal',
    },
    {
        'kind': 'bool_parsing',
        'loc': ['is_developer'],
        'message': 'Value must be a valid boolean, unable to interpret input',
        'input_value': 'foobar',
        'documentation': 'https://pydantic.dev/errors/#bool_parsing',
    },
]
```

I own the `pydantic.dev` domain and will use it for at least these errors so that even if the docs URL changes, the error will still link to the correct documentation. If developers don't want to show these errors to users, they can always process the errors list and filter out items from each error they don't need or want.

### No pure python implementation ![Image 95: 😦](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f626.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#no-pure-python-implementation "Permanent link")

Since pydantic-core is written in Rust, and I have absolutely no intention of rewriting it in python, pydantic V2 will only work where a binary package can be installed.

pydantic-core will provide binaries in PyPI for (at least):

*   **Linux**: `x86_64`, `aarch64`, `i686`, `armv7l`, `musl-x86_64` & `musl-aarch64`
*   **MacOS**: `x86_64` & `arm64` (except python 3.7)
*   **Windows**: `amd64` & `win32`
*   **Web Assembly**: `wasm32` (pydantic-core is [already](https://github.com/pydantic/pydantic-core/runs/7214195252?check_suite_focus=true) compiled for wasm32 using emscripten and unit tests pass, except where cpython itself has [problems](https://github.com/pyodide/pyodide/issues/2841))

Binaries for pypy are a work in progress and will be added if possible, see [pydantic-core#154](https://github.com/pydantic/pydantic-core/issues/154).

Other binaries can be added provided they can be (cross-)compiled on github actions. If no binary is available from PyPI, pydantic-core can be compiled from source if Rust stable is available.

The only place where I know this will cause problems is Raspberry Pi, which is a [mess](https://github.com/piwheels/packages/issues/254) when it comes to packages written in Rust for Python. Effectively, until that's fixed you'll likely have to install pydantic with `pip install -i https://pypi.org/simple/ pydantic`.

### Pydantic becomes a pure python package ![Image 96: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#pydantic-becomes-a-pure-python-package "Permanent link")

Pydantic V1.X is a pure python code base but is compiled with cython to provide some performance improvements. Since the "hot" code is moved to pydantic-core, pydantic itself can go back to being a pure python package.

This should significantly reduce the size of the pydantic package and make unit tests of pydantic much faster. In addition:

*   some constraints on pydantic code can be removed once it no-longer has to be compilable with cython
*   debugging will be easier as you'll be able to drop straight into the pydantic codebase as you can with other, pure python packages

Some pieces of edge logic could get a little slower as they're no longer compiled.

### `is_instance` like checks ![Image 97: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#is_instance-like-checks "Permanent link")

Strict mode also means it makes sense to provide an `is_instance` method on models which effectively run validation then throws away the result while avoiding the (admittedly small) overhead of creating and raising an error or returning the validation result.

To be clear, this isn't a real `isinstance` call, rather it is equivalent to

is\_instance

```
class BaseModel:
    ...

    @classmethod
    def model_is_instance(cls, data: Any) -> bool:
        try:
            cls(**data)
        except ValidationError:
            return False
        else:
            return True
```

### I'm dropping the word "parse" and just using "validate" ![Image 98: 😐](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f610.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#im-dropping-the-word-parse-and-just-using-validate "Permanent link")

Partly due to the issues with the lack of strict mode, I've gone back and forth between using the terms "parse" and "validate" for what pydantic does.

While pydantic is not simply a validation library (and I'm sure some would argue validation is not strictly what it does), most people use the word **"validation"**.

It's time to stop fighting that, and use consistent names.

The word "parse" will no longer be used except when talking about JSON parsing, see [model methods](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#model-namespace-cleanup) above.

### Changes to custom field types ![Image 99: 😐](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f610.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#changes-to-custom-field-types "Permanent link")

Since the core structure of validators has changed from "a list of validators to call one after another" to "a tree of validators which call each other", the [`__get_validators__`](https://docs.pydantic.dev/usage/types/#classes-with-__get_validators__) way of defining custom field types no longer makes sense.

Instead, we'll look for the attribute `__pydantic_validation_schema__` which must be a pydantic-core compliant schema for validating data to this field type (the `function` item can be a string, if so a function of that name will be taken from the class, see `'validate'` below).

Here's an example of how a custom field type could be defined:

New custom field types

```
from pydantic import ValidationSchema

class Foobar:
    def __init__(self, value: str):
        self.value = value

    __pydantic_validation_schema__: ValidationSchema = {
        'type': 'function',
        'mode': 'after',
        'function': 'validate',
        'schema': {'type': 'str'},
    }

    @classmethod
    def validate(cls, value):
        if 'foobar' in value:
            return Foobar(value)
        else:
            raise ValueError('expected foobar')
```

What's going on here: `__pydantic_validation_schema__` defines a schema which effectively says:

> Validate input data as a string, then call the `validate` function with that string, use the returned value as the final result of validation.

`ValidationSchema` is just an alias to [`pydantic_core.Schema`](https://github.com/pydantic/pydantic-core/blob/main/pydantic_core/_types.py#L291) which is a type defining the schema for validation schemas.

Note

pydantic-core schema has full type definitions although since the type is recursive, mypy can't provide static type analysis, pyright however can.

We can probably provide one or more helper functions to make `__pydantic_validation_schema__` easier to generate.

Other Improvements ![Image 100: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#other-improvements "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Some other things which will also change, IMHO for the better:

1.  Recursive models with cyclic references - although recursive models were supported by pydantic V1, data with cyclic references caused recursion errors, in pydantic-core cyclic references are correctly detected and a validation error is raised
2.  The reason I've been so keen to get pydantic-core to compile and run with wasm is that I want all examples in the docs of pydantic V2 to be editable and runnable in the browser
3.  Full support for `TypedDict`, including `total=False` - e.g. omitted keys, providing validation schema to a `TypedDict` field/item will use `Annotated`, e.g. `Annotated[str, Field(strict=True)]`
4.  `from_orm` has become `from_attributes` and is now defined at schema generation time (either via model config or field config)
5.  `input_value` has been added to each line error in a `ValidationError`, making errors easier to understand, and more comprehensive details of errors to be provided to end users, [pydantic#784](https://github.com/pydantic/pydantic/issues/784)
6.  `on_error` logic in a schema which allows either a default value to be used in the event of an error, or that value to be omitted (in the case of a `total=False` `TypedDict`), [pydantic-core#151](https://github.com/pydantic/pydantic-core/issues/151)
7.  `datetime`, `date`, `time` & `timedelta` validation is improved, see the [speedate](https://docs.rs/speedate/latest/speedate/) Rust library I built specifically for this purpose for more details
8.  Powerful "priority" system for optionally merging or overriding config in sub-models for nested schemas
9.  Pydantic will support [annotated-types](https://github.com/annotated-types/annotated-types), so you can do stuff like `Annotated[set[int], Len(0, 10)]` or `Name = Annotated[str, Len(1, 1024)]`
10.  A single decorator for general usage - we should add a `validate` decorator which can be used:
11.  on functions (replacing `validate_arguments`)
12.  on dataclasses, `pydantic.dataclasses.dataclass` will become an alias of this
13.  on `TypedDict`s
14.  On any supported type, e.g. `Union[...]`, `Dict[str, Thing]`
15.  On Custom field types - e.g. anything with a `__pydantic_schema__` attribute
16.  Easier validation error creation, I've often found myself wanting to raise `ValidationError`s outside models, particularly in FastAPI ([here](https://github.com/samuelcolvin/foxglove/blob/a4aaacf372178f345e5ff1d569ee8fd9d10746a4/foxglove/exceptions.py#L137-L149) is one method I've used), we should provide utilities to generate these errors
17.  Improve the performance of `__eq__` on models
18.  Computed fields, these having been an idea for a long time in pydantic - we should get them right
19.  Model validation that avoids instances of subclasses leaking data (particularly important for FastAPI), see [pydantic-core#155](https://github.com/pydantic/pydantic-core/issues/155)
20.  We'll now follow [semvar](https://semver.org/) properly and avoid breaking changes between minor versions, as a result, major versions will become more common
21.  Improve generics to use `M(Basemodel, Generic[T])` instead of `M(GenericModel, Generic[T])` - e.g. `GenericModel` can be removed; this results from no-longer needing to compile pydantic code with cython

Removed Features & Limitations ![Image 101: 😦](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f626.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#removed-features-limitations "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The emoji here is just for variation, I'm not frowning about any of this, these changes are either good IMHO (will make pydantic cleaner, easier to learn and easier to maintain) or irrelevant to 99.9+% of users.

1.  `__root__` custom root models are no longer necessary since validation on any supported data type is allowed without a model
2.  `.parse_file()` and `.parse_raw()`, partially replaced with `.model_validate_json()`, see [model methods](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#model-namespace-cleanup)
3.  `.schema_json()` & `.copy()`, see [model methods](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#model-namespace-cleanup)
4.  `TypeError` are no longer considered as validation errors, but rather as internal errors, this is to better catch errors in argument names in function validators.
5.  Subclasses of builtin types like `str`, `bytes` and `int` are coerced to their parent builtin type, this is a limitation of how pydantic-core converts these types to Rust types during validation, if you have a specific need to keep the type, you can use wrap validators or custom type validation as described above
6.  integers are represented in rust code as `i64`, meaning if you want to use ints where `abs(v) > 2^63 − 1` (9,223,372,036,854,775,807), you'll need to use a [wrap validator](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#validator-function-improvements) and your own logic
7.  [Settings Management](https://docs.pydantic.dev/usage/settings/) ??? - I definitely don't want to remove the functionality, but it's something of a historical curiosity that it lives within pydantic, perhaps it should move to a separate package, perhaps installable alongside pydantic with `pip install pydantic[settings]`?
8.  The following `Config` properties will be removed:
9.  `fields` - it's very old (it pre-dates `Field`), can be removed
10.  `allow_mutation` will be removed, instead `frozen` will be used
11.  `error_msg_templates`, it's not properly documented anyway, error messages can be customized with external logic if required
12.  `getter_dict` - pydantic-core has hardcoded `from_attributes` logic
13.  `json_loads` - again this is hard coded in pydantic-core
14.  `json_dumps` - possibly
15.  `json_encoders` - see the export "mode" discussion [above](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#improvements-to-dumpingserializationexport)
16.  `underscore_attrs_are_private` we should just choose a sensible default
17.  `smart_union` - all unions are now "smart"
18.  `dict(model)` functionality should be removed, there's a much clearer distinction now that in 2017 when I implemented this between a model and a dict

Features Remaining ![Image 102: 😐](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f610.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#features-remaining "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following features will remain (mostly) unchanged:

*   JSONSchema, internally this will need to change a lot, but hopefully the external interface will remain unchanged
*   `dataclass` support, again internals might change, but not the external interface
*   `validate_arguments`, might be renamed, but otherwise remain
*   hypothesis plugin, might be able to improve this as part of the general cleanup

Questions ![Image 103: ❓](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/2753.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#questions "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I hope the explanation above is useful. I'm sure people will have questions and feedback; I'm aware I've skipped over some features with limited detail (this post is already fairly long ![Image 104: 😴](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f634.svg)).

To allow feedback without being overwhelmed, I've created a "Pydantic V2" category for [discussions on github](https://github.com/pydantic/pydantic/discussions/categories/pydantic-v2) - please feel free to create a discussion if you have any questions or suggestions. We will endeavour to read and respond to everyone.

* * *

Implementation Details ![Image 105: 🤓](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f913.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#implementation-details "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

(This is yet to be built, so these are nascent ideas which might change)

At the center of pydantic v2 will be a `PydanticValidator` class which looks roughly like this (note: this is just pseudo-code, it's not even valid python and is only supposed to be used to demonstrate the idea):

PydanticValidator

```
# type identifying data which has been validated,
# as per pydantic-core, this can include "fields_set" data
ValidData = ...

# any type we can perform validation for
AnyOutputType = ...

class PydanticValidator:
    def __init__(self, output_type: AnyOutputType, config: Config):
        ...
    def validate(self, input_data: Any) -> ValidData:
        ...
    def validate_json(self, input_data: str | bytes | bytearray) -> ValidData:
        ...
    def is_instance(self, input_data: Any) -> bool:
        ...
    def is_instance_json(self, input_data: str | bytes | bytearray) -> bool:
        ...
    def json_schema(self) -> dict:
        ...
    def dump(
        self,
        data: ValidData,
        include: ... = None,
        exclude: ... = None,
        by_alias: bool = False,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        mode: Literal['unchanged', 'dicts', 'json-compliant'] = 'unchanged',
        converter: Callable[[Any], Any] | None = None
    ) -> Any:
        ...
    def dump_json(self, ...) -> str:
        ...
```

This could be used directly, but more commonly will be used by the following:

*   `BaseModel`
*   the `validate` decorator described above
*   `pydantic.dataclasses.dataclass` (which might be an alias of `validate`)
*   generics

The aim will be to get pydantic V2 to a place were the vast majority of tests continue to pass unchanged.

Thereby guaranteeing (as much as possible) that the external interface to pydantic and its behaviour are unchanged.

Conversion Table [¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#conversion-table "Permanent link")
-------------------------------------------------------------------------------------------------------

The table below provisionally defines what input value types are allowed to which field types.

**An updated and complete version of this table is available in [V2 conversion table](https://docs.pydantic.dev/2.0/usage/conversion_table/)**.

Note

Some type conversion shown here is a significant departure from existing behavior, we may have to provide a config flag for backwards compatibility for a few of them, however pydantic V2 cannot be entirely backward compatible, see [pydantic-core#152](https://github.com/pydantic/pydantic-core/issues/152).

| Field Type | Input | Mode | Input Source | Conditions |
| --- | --- | --- | --- | --- |
| `str` | `str` | both | python, JSON | \- |
| `str` | `bytes` | lax | python | assumes UTF-8, error on unicode decoding error |
| `str` | `bytearray` | lax | python | assumes UTF-8, error on unicode decoding error |
| `bytes` | `bytes` | both | python | \- |
| `bytes` | `str` | both | JSON | \- |
| `bytes` | `str` | lax | python | \- |
| `bytes` | `bytearray` | lax | python | \- |
| `int` | `int` | strict | python, JSON | max abs value 2^64 - `i64` is used internally, `bool` explicitly forbidden |
| `int` | `int` | lax | python, JSON | `i64` |
| `int` | `float` | lax | python, JSON | `i64`, must be exact int, e.g. `f % 1 == 0`, `nan`, `inf` raise errors |
| `int` | `Decimal` | lax | python, JSON | `i64`, must be exact int, e.g. `f % 1 == 0` |
| `int` | `bool` | lax | python, JSON | \- |
| `int` | `str` | lax | python, JSON | `i64`, must be numeric only, e.g. `[0-9]+` |
| `float` | `float` | strict | python, JSON | `bool` explicitly forbidden |
| `float` | `float` | lax | python, JSON | \- |
| `float` | `int` | lax | python, JSON | \- |
| `float` | `str` | lax | python, JSON | must match `[0-9]+(\.[0-9]+)?` |
| `float` | `Decimal` | lax | python | \- |
| `float` | `bool` | lax | python, JSON | \- |
| `bool` | `bool` | both | python, JSON | \- |
| `bool` | `int` | lax | python, JSON | allowed: `0, 1` |
| `bool` | `float` | lax | python, JSON | allowed: `0, 1` |
| `bool` | `Decimal` | lax | python, JSON | allowed: `0, 1` |
| `bool` | `str` | lax | python, JSON | allowed: `'f', 'n', 'no', 'off', 'false', 't', 'y', 'on', 'yes', 'true'` |
| `None` | `None` | both | python, JSON | \- |
| `date` | `date` | both | python | \- |
| `date` | `datetime` | lax | python | must be exact date, eg. no H, M, S, f |
| `date` | `str` | both | JSON | format `YYYY-MM-DD` |
| `date` | `str` | lax | python | format `YYYY-MM-DD` |
| `date` | `bytes` | lax | python | format `YYYY-MM-DD` (UTF-8) |
| `date` | `int` | lax | python, JSON | interpreted as seconds or ms from epoch, see [speedate](https://docs.rs/speedate/latest/speedate/), must be exact date |
| `date` | `float` | lax | python, JSON | interpreted as seconds or ms from epoch, see [speedate](https://docs.rs/speedate/latest/speedate/), must be exact date |
| `datetime` | `datetime` | both | python | \- |
| `datetime` | `date` | lax | python | \- |
| `datetime` | `str` | both | JSON | format `YYYY-MM-DDTHH:MM:SS.f` etc. see [speedate](https://docs.rs/speedate/latest/speedate/) |
| `datetime` | `str` | lax | python | format `YYYY-MM-DDTHH:MM:SS.f` etc. see [speedate](https://docs.rs/speedate/latest/speedate/) |
| `datetime` | `bytes` | lax | python | format `YYYY-MM-DDTHH:MM:SS.f` etc. see [speedate](https://docs.rs/speedate/latest/speedate/), (UTF-8) |
| `datetime` | `int` | lax | python, JSON | interpreted as seconds or ms from epoch, see [speedate](https://docs.rs/speedate/latest/speedate/) |
| `datetime` | `float` | lax | python, JSON | interpreted as seconds or ms from epoch, see [speedate](https://docs.rs/speedate/latest/speedate/) |
| `time` | `time` | both | python | \- |
| `time` | `str` | both | JSON | format `HH:MM:SS.FFFFFF` etc. see [speedate](https://docs.rs/speedate/latest/speedate/) |
| `time` | `str` | lax | python | format `HH:MM:SS.FFFFFF` etc. see [speedate](https://docs.rs/speedate/latest/speedate/) |
| `time` | `bytes` | lax | python | format `HH:MM:SS.FFFFFF` etc. see [speedate](https://docs.rs/speedate/latest/speedate/), (UTF-8) |
| `time` | `int` | lax | python, JSON | interpreted as seconds, range 0 - 86399 |
| `time` | `float` | lax | python, JSON | interpreted as seconds, range 0 - 86399.9\* |
| `time` | `Decimal` | lax | python, JSON | interpreted as seconds, range 0 - 86399.9\* |
| `timedelta` | `timedelta` | both | python | \- |
| `timedelta` | `str` | both | JSON | format ISO8601 etc. see [speedate](https://docs.rs/speedate/latest/speedate/) |
| `timedelta` | `str` | lax | python | format ISO8601 etc. see [speedate](https://docs.rs/speedate/latest/speedate/) |
| `timedelta` | `bytes` | lax | python | format ISO8601 etc. see [speedate](https://docs.rs/speedate/latest/speedate/), (UTF-8) |
| `timedelta` | `int` | lax | python, JSON | interpreted as seconds |
| `timedelta` | `float` | lax | python, JSON | interpreted as seconds |
| `timedelta` | `Decimal` | lax | python, JSON | interpreted as seconds |
| `dict` | `dict` | both | python | \- |
| `dict` | `Object` | both | JSON | \- |
| `dict` | `mapping` | lax | python | must implement the mapping interface and have an `items()` method |
| `TypedDict` | `dict` | both | python | \- |
| `TypedDict` | `Object` | both | JSON | \- |
| `TypedDict` | `Any` | both | python | builtins not allowed, uses `getattr`, requires `from_attributes=True` |
| `TypedDict` | `mapping` | lax | python | must implement the mapping interface and have an `items()` method |
| `list` | `list` | both | python | \- |
| `list` | `Array` | both | JSON | \- |
| `list` | `tuple` | lax | python | \- |
| `list` | `set` | lax | python | \- |
| `list` | `frozenset` | lax | python | \- |
| `list` | `dict_keys` | lax | python | \- |
| `tuple` | `tuple` | both | python | \- |
| `tuple` | `Array` | both | JSON | \- |
| `tuple` | `list` | lax | python | \- |
| `tuple` | `set` | lax | python | \- |
| `tuple` | `frozenset` | lax | python | \- |
| `tuple` | `dict_keys` | lax | python | \- |
| `set` | `set` | both | python | \- |
| `set` | `Array` | both | JSON | \- |
| `set` | `list` | lax | python | \- |
| `set` | `tuple` | lax | python | \- |
| `set` | `frozenset` | lax | python | \- |
| `set` | `dict_keys` | lax | python | \- |
| `frozenset` | `frozenset` | both | python | \- |
| `frozenset` | `Array` | both | JSON | \- |
| `frozenset` | `list` | lax | python | \- |
| `frozenset` | `tuple` | lax | python | \- |
| `frozenset` | `set` | lax | python | \- |
| `frozenset` | `dict_keys` | lax | python | \- |
| `is_instance` | `Any` | both | python | `isinstance()` check returns `True` |
| `is_instance` | \- | both | JSON | never valid |
| `callable` | `Any` | both | python | `callable()` check returns `True` |
| `callable` | \- | both | JSON | never valid |

The `ModelClass` validator (use to create instances of a class) uses the `TypedDict` validator, then creates an instance with `__dict__` and `__fields_set__` set, so same rules apply as `TypedDict`.

## Metadata

```json
{
  "title": "Pydantic V2 Plan - Pydantic",
  "description": "Data validation using Python type hints",
  "url": "https://docs.pydantic.dev/2.0/blog/pydantic-v2/",
  "content": "* * *\n\nUpdated late 10 Jul 2022, see [pydantic#4226](https://github.com/pydantic/pydantic/pull/4226).\n\n* * *\n\nI've spoken to quite a few people about pydantic V2, and mention it in passing even more.\n\nI owe people a proper explanation of the plan for V2:\n\n*   What we will add\n*   What we will remove\n*   What we will change\n*   How I'm intending to go about completing it and getting it released\n*   Some idea of timeframe ![Image 72: 😨](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f628.svg)\n\nHere goes...\n\n* * *\n\nEnormous thanks to [Eric Jolibois](https://github.com/PrettyWood), [Laurence Watson](https://github.com/Rabscuttler), [Sebastián Ramírez](https://github.com/tiangolo), [Adrian Garcia Badaracco](https://github.com/adriangb), [Tom Hamilton Stubber](https://github.com/tomhamiltonstubber), [Zac Hatfield-Dodds](https://github.com/Zac-HD), [Tom](https://github.com/czotomo) & [Hasan Ramezani](https://github.com/hramezani) for reviewing this blog post, putting up with (and correcting) my horrible typos and making great suggestions that have made this post and Pydantic V2 materially better.\n\n* * *\n\nPlan & Timeframe[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#plan-timeframe \"Permanent link\")\n----------------------------------------------------------------------------------------------------\n\nI'm currently taking a kind of sabbatical after leaving my last job to get pydantic V2 released. Why? I ask myself that question quite often. I'm very proud of how much pydantic is used, but I'm less proud of its internals. Since it's something people seem to care about and use quite a lot (26m downloads a month, used by 72k public repos, 10k stars). I want it to be as good as possible.\n\nWhile I'm on the subject of why, how and my odd sabbatical: if you work for a large company who use pydantic a lot, you might encourage the company to **sponsor me a meaningful amount**, like [Salesforce did](https://twitter.com/samuel_colvin/status/1501288247670063104) (if your organisation is not open to donations, I can also offer consulting services). This is not charity, recruitment or marketing - the argument should be about how much the company will save if pydantic is 10x faster, more stable and more powerful - it would be worth paying me 10% of that to make it happen.\n\nBefore pydantic V2 can be released, we need to release pydantic V1.10 - there are lots of changes in the main branch of pydantic contributed by the community, it's only fair to provide a release including those changes, many of them will remain unchanged for V2, the rest will act as a requirement to make sure pydantic V2 includes the capabilities they implemented.\n\nThe basic road map for me is as follows:\n\n1.  Implement a few more features in pydantic-core, and release a first version, see [below](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#motivation-pydantic-core)\n2.  Work on getting pydantic V1.10 out - basically merge all open PRs that are finished\n3.  Release pydantic V1.10\n4.  Delete all stale PRs which didn't make it into V1.10, apologise profusely to their authors who put their valuable time into pydantic only to have their PRs closed ![Image 73: 🙏](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f64f.svg) (and explain when and how they can rebase and recreate the PR)\n5.  Rename `master` to `main`, seems like a good time to do this\n6.  Change the main branch of pydantic to target V2\n7.  Start tearing pydantic code apart and see how many existing tests can be made to pass\n8.  Rinse, repeat\n9.  Release pydantic V2 ![Image 74: 🎉](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f389.svg)\n\nPlan is to have all this done by the end of October, definitely by the end of the year.\n\n### Breaking Changes & Compatibility ![Image 75: 🙏](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f64f.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#breaking-changes-compatibility \"Permanent link\")\n\nWhile we'll do our best to avoid breaking changes, some things will break.\n\nAs per the [greatest pun in modern TV history](https://youtu.be/ezAlySFluEk).\n\n> You can't make a Tomelette without breaking some Greggs.\n\nWhere possible, if breaking changes are unavoidable, we'll try to provide warnings or errors to make sure those changes are obvious to developers.\n\nMotivation & `pydantic-core`[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#motivation-pydantic-core \"Permanent link\")\n--------------------------------------------------------------------------------------------------------------------------\n\nSince pydantic's initial release, with the help of wonderful contributors [Eric Jolibois](https://github.com/PrettyWood), [Sebastián Ramírez](https://github.com/tiangolo), [David Montague](https://github.com/dmontagu) and many others, the package and its usage have grown enormously. The core logic however has remained mostly unchanged since the initial experiment. It's old, it smells, it needs to be rebuilt.\n\nThe release of version 2 is an opportunity to rebuild pydantic and correct many things that don't make sense - **to make pydantic amazing ![Image 76: 🚀](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f680.svg)** .\n\nThe core validation logic of pydantic V2 will be performed by a separate package [pydantic-core](https://github.com/pydantic/pydantic-core) which I've been building over the last few months. _pydantic-core_ is written in Rust using the excellent [pyo3](https://pyo3.rs/) library which provides rust bindings for python.\n\nThe motivation for building pydantic-core in Rust is as follows:\n\n1.  **Performance**, see [below](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#performance)\n2.  **Recursion and code separation** - with no stack and little-to-no overhead for extra function calls, Rust allows pydantic-core to be implemented as a tree of small validators which call each other, making code easier to understand and extend without harming performance\n3.  **Safety and complexity** - pydantic-core is a fairly complex piece of code which has to draw distinctions between many different errors, Rust is great in situations like this, it should minimise bugs (![Image 77: 🤞](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f91e.svg)) and allow the codebase to be extended for a long time to come\n\nNote\n\nThe python interface to pydantic shouldn't change as a result of using pydantic-core, instead pydantic will use type annotations to build a schema for pydantic-core to use.\n\npydantic-core is usable now, albeit with an unintuitive API, if you're interested, please give it a try.\n\npydantic-core provides validators for common data types, [see a list here](https://github.com/pydantic/pydantic-core/blob/main/pydantic_core/schema_types.py#L314). Other, less commonly used data types will be supported via validator functions implemented in pydantic, in Python.\n\nSee [pydantic-core#153](https://github.com/pydantic/pydantic-core/issues/153) for a summary of what needs to be completed before its first release.\n\nHeadlines[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#headlines \"Permanent link\")\n----------------------------------------------------------------------------------------\n\nHere are some of the biggest changes expected in V2.\n\n### Performance ![Image 78: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#performance \"Permanent link\")\n\nAs a result of the move to Rust for the validation logic (and significant improvements in how validation objects are structured) pydantic V2 will be significantly faster than pydantic V1.\n\nLooking at the pydantic-core [benchmarks](https://github.com/pydantic/pydantic-core/tree/main/tests/benchmarks) today, pydantic V2 is between 4x and 50x faster than pydantic V1.9.1.\n\nIn general, pydantic V2 is about 17x faster than V1 when validating a model containing a range of common fields.\n\n### Strict Mode ![Image 79: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#strict-mode \"Permanent link\")\n\nPeople have long complained about pydantic for coercing data instead of throwing an error. E.g. input to an `int` field could be `123` or the string `\"123\"` which would be converted to `123` While this is very useful in many scenarios (think: URL parameters, environment variables, user input), there are some situations where it's not desirable.\n\npydantic-core comes with \"strict mode\" built in. With this, only the exact data type is allowed, e.g. passing `\"123\"` to an `int` field would result in a validation error.\n\nThis will allow pydantic V2 to offer a `strict` switch which can be set on either a model or a field.\n\n### Formalised Conversion Table ![Image 80: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#formalised-conversion-table \"Permanent link\")\n\nAs well as complaints about coercion, another legitimate complaint was inconsistency around data conversion.\n\nIn pydantic V2, the following principle will govern when data should be converted in \"lax mode\" (`strict=False`):\n\n> If the input data has a SINGLE and INTUITIVE representation, in the field's type, AND no data is lost during the conversion, then the data will be converted; otherwise a validation error is raised. There is one exception to this rule: string fields - virtually all data has an intuitive representation as a string (e.g. `repr()` and `str()`), therefore a custom rule is required: only `str`, `bytes` and `bytearray` are valid as inputs to string fields.\n\nSome examples of what that means in practice:\n\n| Field Type | Input | Single & Intuitive R. | All Data Preserved | Result |\n| --- | --- | --- | --- | --- |\n| `int` | `\"123\"` |  |  | Convert |\n| `int` | `123.0` |  |  | Convert |\n| `int` | `123.1` |  |  | Error |\n| `date` | `\"2020-01-01\"` |  |  | Convert |\n| `date` | `\"2020-01-01T00:00:00\"` |  |  | Convert |\n| `date` | `\"2020-01-01T12:00:00\"` |  |  | Error |\n| `int` | `b\"1\"` |  |  | Error |\n\n(For the last case converting `bytes` to an `int` could reasonably mean `int(bytes_data.decode())` or `int.from_bytes(b'1', 'big/little')`, hence an error)\n\nIn addition to the general rule, we'll provide a conversion table which defines exactly what data will be allowed to which field types. See [the table below](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#conversion-table) for a start on this.\n\n### Built in JSON support ![Image 81: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#built-in-json-support \"Permanent link\")\n\npydantic-core can parse JSON directly into a model or output type, this both improves performance and avoids issue with strictness - e.g. if you have a strict model with a `datetime` field, the input must be a `datetime` object, but clearly that makes no sense when parsing JSON which has no `datatime` type. Same with `bytes` and many other types.\n\nPydantic V2 will therefore allow some conversion when validating JSON directly, even in strict mode (e.g. `ISO8601 string -> datetime`, `str -> bytes`) even though this would not be allowed when validating a python object.\n\nIn future direct validation of JSON will also allow:\n\n*   parsing in a separate thread while starting validation in the main thread\n*   line numbers from JSON to be included in the validation errors\n\n(These features will not be included in V2, but instead will hopefully be added later.)\n\nNote\n\nPydantic has always had special support for JSON, that is not going to change.\n\nWhile in theory other formats could be specifically supported, the overheads and development time are significant and I don't think there's another format that's used widely enough to be worth specific logic. Other formats can be parsed to python then validated, similarly when serializing, data can be exported to a python object, then serialized, see [below](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#improvements-to-dumpingserializationexport).\n\n### Validation without a Model ![Image 82: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#validation-without-a-model \"Permanent link\")\n\nIn pydantic V1 the core of all validation was a pydantic model, this led to a significant performance penalty and extra complexity when the output data type was not a model.\n\npydantic-core operates on a tree of validators with no \"model\" type required at the base of that tree. It can therefore validate a single `string` or `datetime` value, a `TypedDict` or a `Model` equally easily.\n\nThis feature will provide significant addition performance improvements in scenarios like:\n\n*   Adding validation to `dataclasses`\n*   Validating URL arguments, query strings, headers, etc. in FastAPI\n*   Adding validation to `TypedDict`\n*   Function argument validation\n*   Adding validation to your custom classes, decorators...\n\nIn effect - anywhere where you don't care about a traditional model class instance.\n\nWe'll need to add standalone methods for generating JSON Schema and dumping these objects to JSON, etc.\n\n### Required vs. Nullable Cleanup ![Image 83: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#required-vs-nullable-cleanup \"Permanent link\")\n\nPydantic previously had a somewhat confused idea about \"required\" vs. \"nullable\". This mostly resulted from my misgivings about marking a field as `Optional[int]` but requiring a value to be provided but allowing it to be `None` - I didn't like using the word \"optional\" in relation to a field which was not optional.\n\nIn pydantic V2, pydantic will move to match dataclasses, thus:\n\nRequired vs. Nullable\n\n```\nfrom pydantic import BaseModel\n\nclass Foo(BaseModel):\n    f1: str  # required, cannot be None\n    f2: str | None  # required, can be None - same as Optional[str] / Union[str, None]\n    f3: str | None = None  # not required, can be None\n    f4: str = 'Foobar'  # not required, but cannot be None\n```\n\n### Validator Function Improvements ![Image 84: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg) ![Image 85: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg) ![Image 86: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#validator-function-improvements \"Permanent link\")\n\nThis is one of the changes in pydantic V2 that I'm most excited about, I've been talking about something like this for a long time, see [pydantic#1984](https://github.com/pydantic/pydantic/issues/1984), but couldn't find a way to do this until now.\n\nFields which use a function for validation can be any of the following types:\n\n*   **function before mode** - where the function is called before the inner validator is called\n*   **function after mode** - where the function is called after the inner validator is called\n*   **plain mode** - where there's no inner validator\n*   **wrap mode** - where the function takes a reference to a function which calls the inner validator, and can therefore modify the input before inner validation, modify the output after inner validation, conditionally not call the inner validator or catch errors from the inner validator and return a default value, or change the error\n\nAn example how a wrap validator might look:\n\nWrap mode validator function\n\n```\nfrom datetime import datetime\nfrom pydantic import BaseModel, ValidationError, validator\n\nclass MyModel(BaseModel):\n    timestamp: datetime\n\n    @validator('timestamp', mode='wrap')\n    def validate_timestamp(cls, v, handler):\n        if v == 'now':\n            # we don't want to bother with further validation,\n            # just return the new value\n            return datetime.now()\n        try:\n            return handler(v)\n        except ValidationError:\n            # validation failed, in this case we want to\n            # return a default value\n            return datetime(2000, 1, 1)\n```\n\nAs well as being powerful, this provides a great \"escape hatch\" when pydantic validation doesn't do what you need.\n\n### More powerful alias(es) ![Image 87: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#more-powerful-aliases \"Permanent link\")\n\npydantic-core can support alias \"paths\" as well as simple string aliases to flatten data as it's validated.\n\nBest demonstrated with an example:\n\nAlias paths\n\n```\nfrom pydantic import BaseModel, Field\n\nclass Foo(BaseModel):\n    bar: str = Field(aliases=[['baz', 2, 'qux']])\n\ndata = {\n    'baz': [\n        {'qux': 'a'},\n        {'qux': 'b'},\n        {'qux': 'c'},\n        {'qux': 'd'},\n    ]\n}\n\nfoo = Foo(**data)\nassert foo.bar == 'c'\n```\n\n`aliases` is a list of lists because multiple paths can be provided, if so they're tried in turn until a value is found.\n\nTagged unions will use the same logic as `aliases` meaning nested attributes can be used to select a schema to validate against.\n\n### Improvements to Dumping/Serialization/Export ![Image 88: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg) ![Image 89: 😕](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f615.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#improvements-to-dumpingserializationexport \"Permanent link\")\n\n(I haven't worked on this yet, so these ideas are only provisional)\n\nThere has long been a debate about how to handle converting data when extracting it from a model. One of the features people have long requested is the ability to convert data to JSON compliant types while converting a model to a dict.\n\nMy plan is to move data export into pydantic-core, with that, one implementation can support all export modes without compromising (and hopefully significantly improving) performance.\n\nI see four different export/serialization scenarios:\n\n1.  Extracting the field values of a model with no conversion, effectively `model.__dict__` but with the current filtering logic provided by `.dict()`\n2.  Extracting the field values of a model recursively (effectively what `.dict()` does now) - sub-models are converted to dicts, but other fields remain unchanged.\n3.  Extracting data and converting at the same time (e.g. to JSON compliant types)\n4.  Serializing data straight to JSON\n\nI think all 4 modes can be supported in a single implementation, with a kind of \"3.5\" mode where a python function is used to convert the data as the user wishes.\n\nThe current `include` and `exclude` logic is extremely complicated, but hopefully it won't be too hard to translate it to Rust.\n\nWe should also add support for `validate_alias` and `dump_alias` as well as the standard `alias` to allow for customising field keys.\n\n### Validation Context ![Image 90: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#validation-context \"Permanent link\")\n\nPydantic V2 will add a new optional `context` argument to `model_validate` and `model_validate_json` which will allow you to pass information not available when creating a model to validators. See [pydantic#1549](https://github.com/pydantic/pydantic/issues/1549) for motivation.\n\nHere's an example of `context` might be used:\n\nContext during Validation\n\n```\nfrom pydantic import BaseModel, EmailStr, validator\n\nclass User(BaseModel):\n    email: EmailStr\n    home_country: str\n\n    @validator('home_country')\n    def check_home_country(cls, v, context):\n        if v not in context['countries']:\n            raise ValueError('invalid country choice')\n        return v\n\nasync def add_user(post_data: bytes):\n    countries = set(await db_connection.fetch_all('select code from country'))\n    user = User.model_validate_json(post_data, context={'countries': countries})\n    ...\n```\n\nNote\n\nWe (actually mostly Sebastián ![Image 91: 😉](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f609.svg)) will have to make some changes to FastAPI to fully leverage `context` as we'd need some kind of dependency injection to build context before validation so models can still be passed as arguments to views. I'm sure he'll be game.\n\nWarning\n\nAlthough this will make it slightly easier to run synchronous IO (HTTP requests, DB. queries, etc.) from within validators, I strongly advise you keep IO separate from validation - do it before and use context, do it afterwards, avoid where possible making queries inside validation.\n\n### Model Namespace Cleanup ![Image 92: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#model-namespace-cleanup \"Permanent link\")\n\nFor years I've wanted to clean up the model namespace, see [pydantic#1001](https://github.com/pydantic/pydantic/issues/1001). This would avoid confusing gotchas when field names clash with methods on a model, it would also make it safer to add more methods to a model without risking new clashes.\n\nAfter much deliberation (and even giving a lightning talk at the python language submit about alternatives, see [this discussion](https://discuss.python.org/t/better-fields-access-and-allowing-a-new-character-at-the-start-of-identifiers/14529)). I've decided to go with the simplest and clearest approach, at the expense of a bit more typing:\n\nAll methods on models will start with `model_`, fields' names will not be allowed to start with `\"model\"` (aliases can be used if required).\n\nThis will mean `BaseModel` will have roughly the following signature.\n\nNew BaseModel methods\n\n```\nclass BaseModel:\n    model_fields: List[FieldInfo]\n\"\"\"previously `__fields__`, although the format will change a lot\"\"\"\n    @classmethod\n    def model_validate(cls, data: Any, *, context=None) -> Self:  # (1)\n\"\"\"\n        previously `parse_obj()`, validate data\n        \"\"\"\n    @classmethod\n    def model_validate_json(\n        cls,\n        data: str | bytes | bytearray,\n        *,\n        context=None\n    ) -> Self:\n\"\"\"\n        previously `parse_raw(..., content_type='application/json')`\n        validate data from JSON\n        \"\"\"\n    @classmethod\n    def model_is_instance(cls, data: Any, *, context=None) -> bool: # (2)\n\"\"\"\n        new, check if data is value for the model\n        \"\"\"\n    @classmethod\n    def model_is_instance_json(\n        cls,\n        data: str | bytes | bytearray,\n        *,\n        context=None\n    ) -> bool:\n\"\"\"\n        Same as `model_is_instance`, but from JSON\n        \"\"\"\n    def model_dump(\n        self,\n        include: ... = None,\n        exclude: ... = None,\n        by_alias: bool = False,\n        exclude_unset: bool = False,\n        exclude_defaults: bool = False,\n        exclude_none: bool = False,\n        mode: Literal['unchanged', 'dicts', 'json-compliant'] = 'unchanged',\n        converter: Callable[[Any], Any] | None = None\n    ) -> Any:\n\"\"\"\n        previously `dict()`, as before\n        with new `mode` argument\n        \"\"\"\n    def model_dump_json(self, ...) -> str:\n\"\"\"\n        previously `json()`, arguments as above\n        effectively equivalent to `json.dump(self.model_dump(..., mode='json'))`,\n        but more performant\n        \"\"\"\n    def model_json_schema(self, ...) -> dict[str, Any]:\n\"\"\"\n        previously `schema()`, arguments roughly as before\n        JSON schema as a dict\n        \"\"\"\n    def model_update_forward_refs(self) -> None:\n\"\"\"\n        previously `update_forward_refs()`, update forward references\n        \"\"\"\n    @classmethod\n    def model_construct(\n        self,\n        _fields_set: set[str] | None = None,\n        **values: Any\n    ) -> Self:\n\"\"\"\n        previously `construct()`, arguments roughly as before\n        construct a model with no validation\n        \"\"\"\n    @classmethod\n    def model_customize_schema(cls, schema: dict[str, Any]) -> dict[str, Any]:\n\"\"\"\n        new, way to customize validation,\n        e.g. if you wanted to alter how the model validates certain types,\n        or add validation for a specific type without custom types or\n        decorated validators\n        \"\"\"\n    class ModelConfig:\n\"\"\"\n        previously `Config`, configuration class for models\n        \"\"\"\n```\n\n1.  see [Validation Context](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#validation-context) for more information on `context`\n2.  see [`is_instance` checks](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#is_instance-like-checks)\n\nThe following methods will be removed:\n\n*   `.parse_file()` - was a mistake, should never have been in pydantic\n*   `.parse_raw()` - partially replaced by `.model_validate_json()`, the other functionality was a mistake\n*   `.from_orm()` - the functionality has been moved to config, see [other improvements](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#other-improvements) below\n*   `.schema_json()` - mostly since it causes confusion between pydantic validation schema and JSON schema, and can be replaced with just `json.dumps(m.model_json_schema())`\n*   `.copy()` instead we'll implement `__copy__` and let people use the `copy` module (this removes some functionality) from `copy()` but there are bugs and ambiguities with the functionality anyway\n\n### Strict API & API documentation ![Image 93: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#strict-api-api-documentation \"Permanent link\")\n\nWhen preparing for pydantic V2, we'll make a strict distinction between the public API and private functions & classes. Private objects will be clearly identified as private via a `_internal` sub package to discourage use.\n\nThe public API will have API documentation. I've recently been working with the wonderful [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings) package for both [dirty-equals](https://dirty-equals.helpmanual.io/) and [watchfiles](https://watchfiles.helpmanual.io/) documentation. I intend to use `mkdocstrings` to generate complete API documentation for V2.\n\nThis wouldn't replace the current example-based somewhat informal documentation style but instead will augment it.\n\n### Error descriptions ![Image 94: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#error-descriptions \"Permanent link\")\n\nThe way line errors (the individual errors within a `ValidationError`) are built has become much more sophisticated in pydantic-core.\n\nThere's a well-defined [set of error codes and messages](https://github.com/pydantic/pydantic-core/blob/main/src/errors/kinds.rs).\n\nMore will be added when other types are validated via pure python validators in pydantic.\n\nI would like to add a dedicated section to the documentation with extra information for each type of error.\n\nThis would be another key in a line error: `documentation`, which would link to the appropriate section in the docs.\n\nThus, errors might look like:\n\nLine Errors Example\n\n```\n[\n    {\n        'kind': 'greater_than_equal',\n        'loc': ['age'],\n        'message': 'Value must be greater than or equal to 18',\n        'input_value': 11,\n        'context': {'ge': 18},\n        'documentation': 'https://pydantic.dev/errors/#greater_than_equal',\n    },\n    {\n        'kind': 'bool_parsing',\n        'loc': ['is_developer'],\n        'message': 'Value must be a valid boolean, unable to interpret input',\n        'input_value': 'foobar',\n        'documentation': 'https://pydantic.dev/errors/#bool_parsing',\n    },\n]\n```\n\nI own the `pydantic.dev` domain and will use it for at least these errors so that even if the docs URL changes, the error will still link to the correct documentation. If developers don't want to show these errors to users, they can always process the errors list and filter out items from each error they don't need or want.\n\n### No pure python implementation ![Image 95: 😦](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f626.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#no-pure-python-implementation \"Permanent link\")\n\nSince pydantic-core is written in Rust, and I have absolutely no intention of rewriting it in python, pydantic V2 will only work where a binary package can be installed.\n\npydantic-core will provide binaries in PyPI for (at least):\n\n*   **Linux**: `x86_64`, `aarch64`, `i686`, `armv7l`, `musl-x86_64` & `musl-aarch64`\n*   **MacOS**: `x86_64` & `arm64` (except python 3.7)\n*   **Windows**: `amd64` & `win32`\n*   **Web Assembly**: `wasm32` (pydantic-core is [already](https://github.com/pydantic/pydantic-core/runs/7214195252?check_suite_focus=true) compiled for wasm32 using emscripten and unit tests pass, except where cpython itself has [problems](https://github.com/pyodide/pyodide/issues/2841))\n\nBinaries for pypy are a work in progress and will be added if possible, see [pydantic-core#154](https://github.com/pydantic/pydantic-core/issues/154).\n\nOther binaries can be added provided they can be (cross-)compiled on github actions. If no binary is available from PyPI, pydantic-core can be compiled from source if Rust stable is available.\n\nThe only place where I know this will cause problems is Raspberry Pi, which is a [mess](https://github.com/piwheels/packages/issues/254) when it comes to packages written in Rust for Python. Effectively, until that's fixed you'll likely have to install pydantic with `pip install -i https://pypi.org/simple/ pydantic`.\n\n### Pydantic becomes a pure python package ![Image 96: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#pydantic-becomes-a-pure-python-package \"Permanent link\")\n\nPydantic V1.X is a pure python code base but is compiled with cython to provide some performance improvements. Since the \"hot\" code is moved to pydantic-core, pydantic itself can go back to being a pure python package.\n\nThis should significantly reduce the size of the pydantic package and make unit tests of pydantic much faster. In addition:\n\n*   some constraints on pydantic code can be removed once it no-longer has to be compilable with cython\n*   debugging will be easier as you'll be able to drop straight into the pydantic codebase as you can with other, pure python packages\n\nSome pieces of edge logic could get a little slower as they're no longer compiled.\n\n### `is_instance` like checks ![Image 97: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#is_instance-like-checks \"Permanent link\")\n\nStrict mode also means it makes sense to provide an `is_instance` method on models which effectively run validation then throws away the result while avoiding the (admittedly small) overhead of creating and raising an error or returning the validation result.\n\nTo be clear, this isn't a real `isinstance` call, rather it is equivalent to\n\nis\\_instance\n\n```\nclass BaseModel:\n    ...\n\n    @classmethod\n    def model_is_instance(cls, data: Any) -> bool:\n        try:\n            cls(**data)\n        except ValidationError:\n            return False\n        else:\n            return True\n```\n\n### I'm dropping the word \"parse\" and just using \"validate\" ![Image 98: 😐](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f610.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#im-dropping-the-word-parse-and-just-using-validate \"Permanent link\")\n\nPartly due to the issues with the lack of strict mode, I've gone back and forth between using the terms \"parse\" and \"validate\" for what pydantic does.\n\nWhile pydantic is not simply a validation library (and I'm sure some would argue validation is not strictly what it does), most people use the word **\"validation\"**.\n\nIt's time to stop fighting that, and use consistent names.\n\nThe word \"parse\" will no longer be used except when talking about JSON parsing, see [model methods](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#model-namespace-cleanup) above.\n\n### Changes to custom field types ![Image 99: 😐](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f610.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#changes-to-custom-field-types \"Permanent link\")\n\nSince the core structure of validators has changed from \"a list of validators to call one after another\" to \"a tree of validators which call each other\", the [`__get_validators__`](https://docs.pydantic.dev/usage/types/#classes-with-__get_validators__) way of defining custom field types no longer makes sense.\n\nInstead, we'll look for the attribute `__pydantic_validation_schema__` which must be a pydantic-core compliant schema for validating data to this field type (the `function` item can be a string, if so a function of that name will be taken from the class, see `'validate'` below).\n\nHere's an example of how a custom field type could be defined:\n\nNew custom field types\n\n```\nfrom pydantic import ValidationSchema\n\nclass Foobar:\n    def __init__(self, value: str):\n        self.value = value\n\n    __pydantic_validation_schema__: ValidationSchema = {\n        'type': 'function',\n        'mode': 'after',\n        'function': 'validate',\n        'schema': {'type': 'str'},\n    }\n\n    @classmethod\n    def validate(cls, value):\n        if 'foobar' in value:\n            return Foobar(value)\n        else:\n            raise ValueError('expected foobar')\n```\n\nWhat's going on here: `__pydantic_validation_schema__` defines a schema which effectively says:\n\n> Validate input data as a string, then call the `validate` function with that string, use the returned value as the final result of validation.\n\n`ValidationSchema` is just an alias to [`pydantic_core.Schema`](https://github.com/pydantic/pydantic-core/blob/main/pydantic_core/_types.py#L291) which is a type defining the schema for validation schemas.\n\nNote\n\npydantic-core schema has full type definitions although since the type is recursive, mypy can't provide static type analysis, pyright however can.\n\nWe can probably provide one or more helper functions to make `__pydantic_validation_schema__` easier to generate.\n\nOther Improvements ![Image 100: 👍](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f44d.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#other-improvements \"Permanent link\")\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nSome other things which will also change, IMHO for the better:\n\n1.  Recursive models with cyclic references - although recursive models were supported by pydantic V1, data with cyclic references caused recursion errors, in pydantic-core cyclic references are correctly detected and a validation error is raised\n2.  The reason I've been so keen to get pydantic-core to compile and run with wasm is that I want all examples in the docs of pydantic V2 to be editable and runnable in the browser\n3.  Full support for `TypedDict`, including `total=False` - e.g. omitted keys, providing validation schema to a `TypedDict` field/item will use `Annotated`, e.g. `Annotated[str, Field(strict=True)]`\n4.  `from_orm` has become `from_attributes` and is now defined at schema generation time (either via model config or field config)\n5.  `input_value` has been added to each line error in a `ValidationError`, making errors easier to understand, and more comprehensive details of errors to be provided to end users, [pydantic#784](https://github.com/pydantic/pydantic/issues/784)\n6.  `on_error` logic in a schema which allows either a default value to be used in the event of an error, or that value to be omitted (in the case of a `total=False` `TypedDict`), [pydantic-core#151](https://github.com/pydantic/pydantic-core/issues/151)\n7.  `datetime`, `date`, `time` & `timedelta` validation is improved, see the [speedate](https://docs.rs/speedate/latest/speedate/) Rust library I built specifically for this purpose for more details\n8.  Powerful \"priority\" system for optionally merging or overriding config in sub-models for nested schemas\n9.  Pydantic will support [annotated-types](https://github.com/annotated-types/annotated-types), so you can do stuff like `Annotated[set[int], Len(0, 10)]` or `Name = Annotated[str, Len(1, 1024)]`\n10.  A single decorator for general usage - we should add a `validate` decorator which can be used:\n11.  on functions (replacing `validate_arguments`)\n12.  on dataclasses, `pydantic.dataclasses.dataclass` will become an alias of this\n13.  on `TypedDict`s\n14.  On any supported type, e.g. `Union[...]`, `Dict[str, Thing]`\n15.  On Custom field types - e.g. anything with a `__pydantic_schema__` attribute\n16.  Easier validation error creation, I've often found myself wanting to raise `ValidationError`s outside models, particularly in FastAPI ([here](https://github.com/samuelcolvin/foxglove/blob/a4aaacf372178f345e5ff1d569ee8fd9d10746a4/foxglove/exceptions.py#L137-L149) is one method I've used), we should provide utilities to generate these errors\n17.  Improve the performance of `__eq__` on models\n18.  Computed fields, these having been an idea for a long time in pydantic - we should get them right\n19.  Model validation that avoids instances of subclasses leaking data (particularly important for FastAPI), see [pydantic-core#155](https://github.com/pydantic/pydantic-core/issues/155)\n20.  We'll now follow [semvar](https://semver.org/) properly and avoid breaking changes between minor versions, as a result, major versions will become more common\n21.  Improve generics to use `M(Basemodel, Generic[T])` instead of `M(GenericModel, Generic[T])` - e.g. `GenericModel` can be removed; this results from no-longer needing to compile pydantic code with cython\n\nRemoved Features & Limitations ![Image 101: 😦](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f626.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#removed-features-limitations \"Permanent link\")\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nThe emoji here is just for variation, I'm not frowning about any of this, these changes are either good IMHO (will make pydantic cleaner, easier to learn and easier to maintain) or irrelevant to 99.9+% of users.\n\n1.  `__root__` custom root models are no longer necessary since validation on any supported data type is allowed without a model\n2.  `.parse_file()` and `.parse_raw()`, partially replaced with `.model_validate_json()`, see [model methods](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#model-namespace-cleanup)\n3.  `.schema_json()` & `.copy()`, see [model methods](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#model-namespace-cleanup)\n4.  `TypeError` are no longer considered as validation errors, but rather as internal errors, this is to better catch errors in argument names in function validators.\n5.  Subclasses of builtin types like `str`, `bytes` and `int` are coerced to their parent builtin type, this is a limitation of how pydantic-core converts these types to Rust types during validation, if you have a specific need to keep the type, you can use wrap validators or custom type validation as described above\n6.  integers are represented in rust code as `i64`, meaning if you want to use ints where `abs(v) > 2^63 − 1` (9,223,372,036,854,775,807), you'll need to use a [wrap validator](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#validator-function-improvements) and your own logic\n7.  [Settings Management](https://docs.pydantic.dev/usage/settings/) ??? - I definitely don't want to remove the functionality, but it's something of a historical curiosity that it lives within pydantic, perhaps it should move to a separate package, perhaps installable alongside pydantic with `pip install pydantic[settings]`?\n8.  The following `Config` properties will be removed:\n9.  `fields` - it's very old (it pre-dates `Field`), can be removed\n10.  `allow_mutation` will be removed, instead `frozen` will be used\n11.  `error_msg_templates`, it's not properly documented anyway, error messages can be customized with external logic if required\n12.  `getter_dict` - pydantic-core has hardcoded `from_attributes` logic\n13.  `json_loads` - again this is hard coded in pydantic-core\n14.  `json_dumps` - possibly\n15.  `json_encoders` - see the export \"mode\" discussion [above](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#improvements-to-dumpingserializationexport)\n16.  `underscore_attrs_are_private` we should just choose a sensible default\n17.  `smart_union` - all unions are now \"smart\"\n18.  `dict(model)` functionality should be removed, there's a much clearer distinction now that in 2017 when I implemented this between a model and a dict\n\nFeatures Remaining ![Image 102: 😐](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f610.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#features-remaining \"Permanent link\")\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nThe following features will remain (mostly) unchanged:\n\n*   JSONSchema, internally this will need to change a lot, but hopefully the external interface will remain unchanged\n*   `dataclass` support, again internals might change, but not the external interface\n*   `validate_arguments`, might be renamed, but otherwise remain\n*   hypothesis plugin, might be able to improve this as part of the general cleanup\n\nQuestions ![Image 103: ❓](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/2753.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#questions \"Permanent link\")\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nI hope the explanation above is useful. I'm sure people will have questions and feedback; I'm aware I've skipped over some features with limited detail (this post is already fairly long ![Image 104: 😴](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f634.svg)).\n\nTo allow feedback without being overwhelmed, I've created a \"Pydantic V2\" category for [discussions on github](https://github.com/pydantic/pydantic/discussions/categories/pydantic-v2) - please feel free to create a discussion if you have any questions or suggestions. We will endeavour to read and respond to everyone.\n\n* * *\n\nImplementation Details ![Image 105: 🤓](https://cdn.jsdelivr.net/gh/jdecked/twemoji@14.1.2/assets/svg/1f913.svg)[¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#implementation-details \"Permanent link\")\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n(This is yet to be built, so these are nascent ideas which might change)\n\nAt the center of pydantic v2 will be a `PydanticValidator` class which looks roughly like this (note: this is just pseudo-code, it's not even valid python and is only supposed to be used to demonstrate the idea):\n\nPydanticValidator\n\n```\n# type identifying data which has been validated,\n# as per pydantic-core, this can include \"fields_set\" data\nValidData = ...\n\n# any type we can perform validation for\nAnyOutputType = ...\n\nclass PydanticValidator:\n    def __init__(self, output_type: AnyOutputType, config: Config):\n        ...\n    def validate(self, input_data: Any) -> ValidData:\n        ...\n    def validate_json(self, input_data: str | bytes | bytearray) -> ValidData:\n        ...\n    def is_instance(self, input_data: Any) -> bool:\n        ...\n    def is_instance_json(self, input_data: str | bytes | bytearray) -> bool:\n        ...\n    def json_schema(self) -> dict:\n        ...\n    def dump(\n        self,\n        data: ValidData,\n        include: ... = None,\n        exclude: ... = None,\n        by_alias: bool = False,\n        exclude_unset: bool = False,\n        exclude_defaults: bool = False,\n        exclude_none: bool = False,\n        mode: Literal['unchanged', 'dicts', 'json-compliant'] = 'unchanged',\n        converter: Callable[[Any], Any] | None = None\n    ) -> Any:\n        ...\n    def dump_json(self, ...) -> str:\n        ...\n```\n\nThis could be used directly, but more commonly will be used by the following:\n\n*   `BaseModel`\n*   the `validate` decorator described above\n*   `pydantic.dataclasses.dataclass` (which might be an alias of `validate`)\n*   generics\n\nThe aim will be to get pydantic V2 to a place were the vast majority of tests continue to pass unchanged.\n\nThereby guaranteeing (as much as possible) that the external interface to pydantic and its behaviour are unchanged.\n\nConversion Table [¶](https://docs.pydantic.dev/2.0/blog/pydantic-v2/#conversion-table \"Permanent link\")\n-------------------------------------------------------------------------------------------------------\n\nThe table below provisionally defines what input value types are allowed to which field types.\n\n**An updated and complete version of this table is available in [V2 conversion table](https://docs.pydantic.dev/2.0/usage/conversion_table/)**.\n\nNote\n\nSome type conversion shown here is a significant departure from existing behavior, we may have to provide a config flag for backwards compatibility for a few of them, however pydantic V2 cannot be entirely backward compatible, see [pydantic-core#152](https://github.com/pydantic/pydantic-core/issues/152).\n\n| Field Type | Input | Mode | Input Source | Conditions |\n| --- | --- | --- | --- | --- |\n| `str` | `str` | both | python, JSON | \\- |\n| `str` | `bytes` | lax | python | assumes UTF-8, error on unicode decoding error |\n| `str` | `bytearray` | lax | python | assumes UTF-8, error on unicode decoding error |\n| `bytes` | `bytes` | both | python | \\- |\n| `bytes` | `str` | both | JSON | \\- |\n| `bytes` | `str` | lax | python | \\- |\n| `bytes` | `bytearray` | lax | python | \\- |\n| `int` | `int` | strict | python, JSON | max abs value 2^64 - `i64` is used internally, `bool` explicitly forbidden |\n| `int` | `int` | lax | python, JSON | `i64` |\n| `int` | `float` | lax | python, JSON | `i64`, must be exact int, e.g. `f % 1 == 0`, `nan`, `inf` raise errors |\n| `int` | `Decimal` | lax | python, JSON | `i64`, must be exact int, e.g. `f % 1 == 0` |\n| `int` | `bool` | lax | python, JSON | \\- |\n| `int` | `str` | lax | python, JSON | `i64`, must be numeric only, e.g. `[0-9]+` |\n| `float` | `float` | strict | python, JSON | `bool` explicitly forbidden |\n| `float` | `float` | lax | python, JSON | \\- |\n| `float` | `int` | lax | python, JSON | \\- |\n| `float` | `str` | lax | python, JSON | must match `[0-9]+(\\.[0-9]+)?` |\n| `float` | `Decimal` | lax | python | \\- |\n| `float` | `bool` | lax | python, JSON | \\- |\n| `bool` | `bool` | both | python, JSON | \\- |\n| `bool` | `int` | lax | python, JSON | allowed: `0, 1` |\n| `bool` | `float` | lax | python, JSON | allowed: `0, 1` |\n| `bool` | `Decimal` | lax | python, JSON | allowed: `0, 1` |\n| `bool` | `str` | lax | python, JSON | allowed: `'f', 'n', 'no', 'off', 'false', 't', 'y', 'on', 'yes', 'true'` |\n| `None` | `None` | both | python, JSON | \\- |\n| `date` | `date` | both | python | \\- |\n| `date` | `datetime` | lax | python | must be exact date, eg. no H, M, S, f |\n| `date` | `str` | both | JSON | format `YYYY-MM-DD` |\n| `date` | `str` | lax | python | format `YYYY-MM-DD` |\n| `date` | `bytes` | lax | python | format `YYYY-MM-DD` (UTF-8) |\n| `date` | `int` | lax | python, JSON | interpreted as seconds or ms from epoch, see [speedate](https://docs.rs/speedate/latest/speedate/), must be exact date |\n| `date` | `float` | lax | python, JSON | interpreted as seconds or ms from epoch, see [speedate](https://docs.rs/speedate/latest/speedate/), must be exact date |\n| `datetime` | `datetime` | both | python | \\- |\n| `datetime` | `date` | lax | python | \\- |\n| `datetime` | `str` | both | JSON | format `YYYY-MM-DDTHH:MM:SS.f` etc. see [speedate](https://docs.rs/speedate/latest/speedate/) |\n| `datetime` | `str` | lax | python | format `YYYY-MM-DDTHH:MM:SS.f` etc. see [speedate](https://docs.rs/speedate/latest/speedate/) |\n| `datetime` | `bytes` | lax | python | format `YYYY-MM-DDTHH:MM:SS.f` etc. see [speedate](https://docs.rs/speedate/latest/speedate/), (UTF-8) |\n| `datetime` | `int` | lax | python, JSON | interpreted as seconds or ms from epoch, see [speedate](https://docs.rs/speedate/latest/speedate/) |\n| `datetime` | `float` | lax | python, JSON | interpreted as seconds or ms from epoch, see [speedate](https://docs.rs/speedate/latest/speedate/) |\n| `time` | `time` | both | python | \\- |\n| `time` | `str` | both | JSON | format `HH:MM:SS.FFFFFF` etc. see [speedate](https://docs.rs/speedate/latest/speedate/) |\n| `time` | `str` | lax | python | format `HH:MM:SS.FFFFFF` etc. see [speedate](https://docs.rs/speedate/latest/speedate/) |\n| `time` | `bytes` | lax | python | format `HH:MM:SS.FFFFFF` etc. see [speedate](https://docs.rs/speedate/latest/speedate/), (UTF-8) |\n| `time` | `int` | lax | python, JSON | interpreted as seconds, range 0 - 86399 |\n| `time` | `float` | lax | python, JSON | interpreted as seconds, range 0 - 86399.9\\* |\n| `time` | `Decimal` | lax | python, JSON | interpreted as seconds, range 0 - 86399.9\\* |\n| `timedelta` | `timedelta` | both | python | \\- |\n| `timedelta` | `str` | both | JSON | format ISO8601 etc. see [speedate](https://docs.rs/speedate/latest/speedate/) |\n| `timedelta` | `str` | lax | python | format ISO8601 etc. see [speedate](https://docs.rs/speedate/latest/speedate/) |\n| `timedelta` | `bytes` | lax | python | format ISO8601 etc. see [speedate](https://docs.rs/speedate/latest/speedate/), (UTF-8) |\n| `timedelta` | `int` | lax | python, JSON | interpreted as seconds |\n| `timedelta` | `float` | lax | python, JSON | interpreted as seconds |\n| `timedelta` | `Decimal` | lax | python, JSON | interpreted as seconds |\n| `dict` | `dict` | both | python | \\- |\n| `dict` | `Object` | both | JSON | \\- |\n| `dict` | `mapping` | lax | python | must implement the mapping interface and have an `items()` method |\n| `TypedDict` | `dict` | both | python | \\- |\n| `TypedDict` | `Object` | both | JSON | \\- |\n| `TypedDict` | `Any` | both | python | builtins not allowed, uses `getattr`, requires `from_attributes=True` |\n| `TypedDict` | `mapping` | lax | python | must implement the mapping interface and have an `items()` method |\n| `list` | `list` | both | python | \\- |\n| `list` | `Array` | both | JSON | \\- |\n| `list` | `tuple` | lax | python | \\- |\n| `list` | `set` | lax | python | \\- |\n| `list` | `frozenset` | lax | python | \\- |\n| `list` | `dict_keys` | lax | python | \\- |\n| `tuple` | `tuple` | both | python | \\- |\n| `tuple` | `Array` | both | JSON | \\- |\n| `tuple` | `list` | lax | python | \\- |\n| `tuple` | `set` | lax | python | \\- |\n| `tuple` | `frozenset` | lax | python | \\- |\n| `tuple` | `dict_keys` | lax | python | \\- |\n| `set` | `set` | both | python | \\- |\n| `set` | `Array` | both | JSON | \\- |\n| `set` | `list` | lax | python | \\- |\n| `set` | `tuple` | lax | python | \\- |\n| `set` | `frozenset` | lax | python | \\- |\n| `set` | `dict_keys` | lax | python | \\- |\n| `frozenset` | `frozenset` | both | python | \\- |\n| `frozenset` | `Array` | both | JSON | \\- |\n| `frozenset` | `list` | lax | python | \\- |\n| `frozenset` | `tuple` | lax | python | \\- |\n| `frozenset` | `set` | lax | python | \\- |\n| `frozenset` | `dict_keys` | lax | python | \\- |\n| `is_instance` | `Any` | both | python | `isinstance()` check returns `True` |\n| `is_instance` | \\- | both | JSON | never valid |\n| `callable` | `Any` | both | python | `callable()` check returns `True` |\n| `callable` | \\- | both | JSON | never valid |\n\nThe `ModelClass` validator (use to create instances of a class) uses the `TypedDict` validator, then creates an instance with `__dict__` and `__fields_set__` set, so same rules apply as `TypedDict`.",
  "usage": {
    "tokens": 13481
  }
}
```
