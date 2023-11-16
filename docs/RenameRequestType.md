# RenameRequestType

The parameters of *ManagedEntity.Rename_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_name** | **str** |  | 

## Example

```python
from vmware_vi.models.rename_request_type import RenameRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RenameRequestType from a JSON string
rename_request_type_instance = RenameRequestType.from_json(json)
# print the JSON string representation of the object
print RenameRequestType.to_json()

# convert the object into a dict
rename_request_type_dict = rename_request_type_instance.to_dict()
# create an instance of RenameRequestType from a dict
rename_request_type_form_dict = rename_request_type.from_dict(rename_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


