# ClearVStorageObjectControlFlagsRequestType

The parameters of *VcenterVStorageObjectManager.ClearVStorageObjectControlFlags*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**control_flags** | **List[str]** | control flags enum array to be cleared on the VStorageObject. All control flags not included in the array remain intact.  | [optional] 

## Example

```python
from vmware_vi.models.clear_v_storage_object_control_flags_request_type import ClearVStorageObjectControlFlagsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ClearVStorageObjectControlFlagsRequestType from a JSON string
clear_v_storage_object_control_flags_request_type_instance = ClearVStorageObjectControlFlagsRequestType.from_json(json)
# print the JSON string representation of the object
print ClearVStorageObjectControlFlagsRequestType.to_json()

# convert the object into a dict
clear_v_storage_object_control_flags_request_type_dict = clear_v_storage_object_control_flags_request_type_instance.to_dict()
# create an instance of ClearVStorageObjectControlFlagsRequestType from a dict
clear_v_storage_object_control_flags_request_type_form_dict = clear_v_storage_object_control_flags_request_type.from_dict(clear_v_storage_object_control_flags_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


