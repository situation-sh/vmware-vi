# UpdateOptionsRequestType

The parameters of *OptionManager.UpdateOptions*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed_value** | [**List[OptionValue]**](OptionValue.md) |  | 

## Example

```python
from vmware_vi.models.update_options_request_type import UpdateOptionsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOptionsRequestType from a JSON string
update_options_request_type_instance = UpdateOptionsRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateOptionsRequestType.to_json()

# convert the object into a dict
update_options_request_type_dict = update_options_request_type_instance.to_dict()
# create an instance of UpdateOptionsRequestType from a dict
update_options_request_type_form_dict = update_options_request_type.from_dict(update_options_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


