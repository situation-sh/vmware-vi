# ArrayOfWaitOptions

A boxed array of *WaitOptions*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[WaitOptions]**](WaitOptions.md) |  | 

## Example

```python
from vmware_vi.models.array_of_wait_options import ArrayOfWaitOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfWaitOptions from a JSON string
array_of_wait_options_instance = ArrayOfWaitOptions.from_json(json)
# print the JSON string representation of the object
print ArrayOfWaitOptions.to_json()

# convert the object into a dict
array_of_wait_options_dict = array_of_wait_options_instance.to_dict()
# create an instance of ArrayOfWaitOptions from a dict
array_of_wait_options_form_dict = array_of_wait_options.from_dict(array_of_wait_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


