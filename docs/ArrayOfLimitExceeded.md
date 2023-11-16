# ArrayOfLimitExceeded

A boxed array of *LimitExceeded*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LimitExceeded]**](LimitExceeded.md) |  | 

## Example

```python
from vmware_vi.models.array_of_limit_exceeded import ArrayOfLimitExceeded

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLimitExceeded from a JSON string
array_of_limit_exceeded_instance = ArrayOfLimitExceeded.from_json(json)
# print the JSON string representation of the object
print ArrayOfLimitExceeded.to_json()

# convert the object into a dict
array_of_limit_exceeded_dict = array_of_limit_exceeded_instance.to_dict()
# create an instance of ArrayOfLimitExceeded from a dict
array_of_limit_exceeded_form_dict = array_of_limit_exceeded.from_dict(array_of_limit_exceeded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


