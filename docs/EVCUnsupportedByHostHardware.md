# EVCUnsupportedByHostHardware

An attempt to enable Enhanced VMotion Compatibility (EVC) on a cluster has failed because one or more hosts in the cluster do not match the desired featureset and lack hardware support for EVC.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The set of hosts which are blocking EVC because their CPU hardware does not support CPUID override.  ***Since:*** vSphere API 4.1  Refers instances of *HostSystem*.  | 
**host_name** | **List[str]** | The names of the hosts in the host array.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.evc_unsupported_by_host_hardware import EVCUnsupportedByHostHardware

# TODO update the JSON string below
json = "{}"
# create an instance of EVCUnsupportedByHostHardware from a JSON string
evc_unsupported_by_host_hardware_instance = EVCUnsupportedByHostHardware.from_json(json)
# print the JSON string representation of the object
print EVCUnsupportedByHostHardware.to_json()

# convert the object into a dict
evc_unsupported_by_host_hardware_dict = evc_unsupported_by_host_hardware_instance.to_dict()
# create an instance of EVCUnsupportedByHostHardware from a dict
evc_unsupported_by_host_hardware_form_dict = evc_unsupported_by_host_hardware.from_dict(evc_unsupported_by_host_hardware_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


