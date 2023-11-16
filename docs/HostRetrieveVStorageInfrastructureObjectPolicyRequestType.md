# HostRetrieveVStorageInfrastructureObjectPolicyRequestType

The parameters of *HostVStorageObjectManager.HostRetrieveVStorageInfrastructureObjectPolicy*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.host_retrieve_v_storage_infrastructure_object_policy_request_type import HostRetrieveVStorageInfrastructureObjectPolicyRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostRetrieveVStorageInfrastructureObjectPolicyRequestType from a JSON string
host_retrieve_v_storage_infrastructure_object_policy_request_type_instance = HostRetrieveVStorageInfrastructureObjectPolicyRequestType.from_json(json)
# print the JSON string representation of the object
print HostRetrieveVStorageInfrastructureObjectPolicyRequestType.to_json()

# convert the object into a dict
host_retrieve_v_storage_infrastructure_object_policy_request_type_dict = host_retrieve_v_storage_infrastructure_object_policy_request_type_instance.to_dict()
# create an instance of HostRetrieveVStorageInfrastructureObjectPolicyRequestType from a dict
host_retrieve_v_storage_infrastructure_object_policy_request_type_form_dict = host_retrieve_v_storage_infrastructure_object_policy_request_type.from_dict(host_retrieve_v_storage_infrastructure_object_policy_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


