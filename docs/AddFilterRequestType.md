# AddFilterRequestType

The parameters of *HealthUpdateManager.AddFilter*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | The provider identifier.  | 
**filter_name** | **str** | The filter name.  | 
**info_ids** | **List[str]** | The list of HealthUpdateInfo IDs that should be filtered.  | [optional] 

## Example

```python
from vmware_vi.models.add_filter_request_type import AddFilterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AddFilterRequestType from a JSON string
add_filter_request_type_instance = AddFilterRequestType.from_json(json)
# print the JSON string representation of the object
print AddFilterRequestType.to_json()

# convert the object into a dict
add_filter_request_type_dict = add_filter_request_type_instance.to_dict()
# create an instance of AddFilterRequestType from a dict
add_filter_request_type_form_dict = add_filter_request_type.from_dict(add_filter_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


