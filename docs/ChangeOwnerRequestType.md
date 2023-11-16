# ChangeOwnerRequestType

The parameters of *FileManager.ChangeOwner*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**owner** | **str** |  | 

## Example

```python
from vmware_vi.models.change_owner_request_type import ChangeOwnerRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeOwnerRequestType from a JSON string
change_owner_request_type_instance = ChangeOwnerRequestType.from_json(json)
# print the JSON string representation of the object
print ChangeOwnerRequestType.to_json()

# convert the object into a dict
change_owner_request_type_dict = change_owner_request_type_instance.to_dict()
# create an instance of ChangeOwnerRequestType from a dict
change_owner_request_type_form_dict = change_owner_request_type.from_dict(change_owner_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


