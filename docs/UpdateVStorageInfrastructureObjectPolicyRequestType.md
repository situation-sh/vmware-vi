# UpdateVStorageInfrastructureObjectPolicyRequestType

The parameters of *VcenterVStorageObjectManager.UpdateVStorageInfrastructureObjectPolicy_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**VslmInfrastructureObjectPolicySpec**](VslmInfrastructureObjectPolicySpec.md) |  | 

## Example

```python
from vmware_vi.models.update_v_storage_infrastructure_object_policy_request_type import UpdateVStorageInfrastructureObjectPolicyRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVStorageInfrastructureObjectPolicyRequestType from a JSON string
update_v_storage_infrastructure_object_policy_request_type_instance = UpdateVStorageInfrastructureObjectPolicyRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateVStorageInfrastructureObjectPolicyRequestType.to_json()

# convert the object into a dict
update_v_storage_infrastructure_object_policy_request_type_dict = update_v_storage_infrastructure_object_policy_request_type_instance.to_dict()
# create an instance of UpdateVStorageInfrastructureObjectPolicyRequestType from a dict
update_v_storage_infrastructure_object_policy_request_type_form_dict = update_v_storage_infrastructure_object_policy_request_type.from_dict(update_v_storage_infrastructure_object_policy_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


