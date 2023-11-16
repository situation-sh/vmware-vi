# EVCUnsupportedByHostSoftware

An attempt to enable Enhanced VMotion Compatibility (EVC) on a cluster has failed because one or more hosts in the cluster lack software support for EVC.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The set of hosts which are blocking EVC because their virtualization software does not support CPUID override.  ***Since:*** vSphere API 4.1  Refers instances of *HostSystem*.  | 
**host_name** | **List[str]** | The names of the hosts in the host array.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.evc_unsupported_by_host_software import EVCUnsupportedByHostSoftware

# TODO update the JSON string below
json = "{}"
# create an instance of EVCUnsupportedByHostSoftware from a JSON string
evc_unsupported_by_host_software_instance = EVCUnsupportedByHostSoftware.from_json(json)
# print the JSON string representation of the object
print EVCUnsupportedByHostSoftware.to_json()

# convert the object into a dict
evc_unsupported_by_host_software_dict = evc_unsupported_by_host_software_instance.to_dict()
# create an instance of EVCUnsupportedByHostSoftware from a dict
evc_unsupported_by_host_software_form_dict = evc_unsupported_by_host_software.from_dict(evc_unsupported_by_host_software_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


