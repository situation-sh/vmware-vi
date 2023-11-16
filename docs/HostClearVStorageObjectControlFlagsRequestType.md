# HostClearVStorageObjectControlFlagsRequestType

The parameters of *HostVStorageObjectManager.HostClearVStorageObjectControlFlags*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**control_flags** | **List[str]** | control flags enum array to be cleared on the VStorageObject. All control flags not included in the array remain intact.  | [optional] 

## Example

```python
from vmware_vi.models.host_clear_v_storage_object_control_flags_request_type import HostClearVStorageObjectControlFlagsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostClearVStorageObjectControlFlagsRequestType from a JSON string
host_clear_v_storage_object_control_flags_request_type_instance = HostClearVStorageObjectControlFlagsRequestType.from_json(json)
# print the JSON string representation of the object
print HostClearVStorageObjectControlFlagsRequestType.to_json()

# convert the object into a dict
host_clear_v_storage_object_control_flags_request_type_dict = host_clear_v_storage_object_control_flags_request_type_instance.to_dict()
# create an instance of HostClearVStorageObjectControlFlagsRequestType from a dict
host_clear_v_storage_object_control_flags_request_type_form_dict = host_clear_v_storage_object_control_flags_request_type.from_dict(host_clear_v_storage_object_control_flags_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


