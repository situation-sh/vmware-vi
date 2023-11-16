# UpdateVStorageObjectPolicyRequestType

The parameters of *VcenterVStorageObjectManager.UpdateVStorageObjectPolicy_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**profile** | [**List[VirtualMachineProfileSpec]**](VirtualMachineProfileSpec.md) | New profile requirement on the virtual storage object.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.update_v_storage_object_policy_request_type import UpdateVStorageObjectPolicyRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVStorageObjectPolicyRequestType from a JSON string
update_v_storage_object_policy_request_type_instance = UpdateVStorageObjectPolicyRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateVStorageObjectPolicyRequestType.to_json()

# convert the object into a dict
update_v_storage_object_policy_request_type_dict = update_v_storage_object_policy_request_type_instance.to_dict()
# create an instance of UpdateVStorageObjectPolicyRequestType from a dict
update_v_storage_object_policy_request_type_form_dict = update_v_storage_object_policy_request_type.from_dict(update_v_storage_object_policy_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


