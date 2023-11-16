# SetVStorageObjectControlFlagsRequestType

The parameters of *VcenterVStorageObjectManager.SetVStorageObjectControlFlags*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**control_flags** | **List[str]** | control flags enum array to be set on the VStorageObject. All control flags not included in the array remain intact.  | [optional] 

## Example

```python
from vmware_vi.models.set_v_storage_object_control_flags_request_type import SetVStorageObjectControlFlagsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetVStorageObjectControlFlagsRequestType from a JSON string
set_v_storage_object_control_flags_request_type_instance = SetVStorageObjectControlFlagsRequestType.from_json(json)
# print the JSON string representation of the object
print SetVStorageObjectControlFlagsRequestType.to_json()

# convert the object into a dict
set_v_storage_object_control_flags_request_type_dict = set_v_storage_object_control_flags_request_type_instance.to_dict()
# create an instance of SetVStorageObjectControlFlagsRequestType from a dict
set_v_storage_object_control_flags_request_type_form_dict = set_v_storage_object_control_flags_request_type.from_dict(set_v_storage_object_control_flags_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


