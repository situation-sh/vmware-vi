# RetrieveVStorageInfrastructureObjectPolicyRequestType

The parameters of *VcenterVStorageObjectManager.RetrieveVStorageInfrastructureObjectPolicy*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.retrieve_v_storage_infrastructure_object_policy_request_type import RetrieveVStorageInfrastructureObjectPolicyRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveVStorageInfrastructureObjectPolicyRequestType from a JSON string
retrieve_v_storage_infrastructure_object_policy_request_type_instance = RetrieveVStorageInfrastructureObjectPolicyRequestType.from_json(json)
# print the JSON string representation of the object
print RetrieveVStorageInfrastructureObjectPolicyRequestType.to_json()

# convert the object into a dict
retrieve_v_storage_infrastructure_object_policy_request_type_dict = retrieve_v_storage_infrastructure_object_policy_request_type_instance.to_dict()
# create an instance of RetrieveVStorageInfrastructureObjectPolicyRequestType from a dict
retrieve_v_storage_infrastructure_object_policy_request_type_form_dict = retrieve_v_storage_infrastructure_object_policy_request_type.from_dict(retrieve_v_storage_infrastructure_object_policy_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


