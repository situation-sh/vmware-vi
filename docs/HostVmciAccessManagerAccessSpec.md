# HostVmciAccessManagerAccessSpec

The AccessSpec data object declares an update to the service access granted to a VM.  The given list of services will either be granted in addition to existing services, replace the existing service or be revoked depending on the mode specified. In case of a revoke, an empty or non-existing service list indicates that all granted services should be revoked.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**services** | **List[str]** |  | [optional] 
**mode** | **str** |  | 

## Example

```python
from vmware_vi.models.host_vmci_access_manager_access_spec import HostVmciAccessManagerAccessSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostVmciAccessManagerAccessSpec from a JSON string
host_vmci_access_manager_access_spec_instance = HostVmciAccessManagerAccessSpec.from_json(json)
# print the JSON string representation of the object
print HostVmciAccessManagerAccessSpec.to_json()

# convert the object into a dict
host_vmci_access_manager_access_spec_dict = host_vmci_access_manager_access_spec_instance.to_dict()
# create an instance of HostVmciAccessManagerAccessSpec from a dict
host_vmci_access_manager_access_spec_form_dict = host_vmci_access_manager_access_spec.from_dict(host_vmci_access_manager_access_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


