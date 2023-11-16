# EVCModeUnsupportedByHosts

An attempt to enable Enhanced VMotion Compatibility on a cluster has failed because there are hosts in the cluster with a CPU feature baseline below the desired EVC mode.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evc_mode** | **str** | The requested EVC mode.  ***Since:*** vSphere API 4.0  | [optional] 
**host** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The set of hosts which are blocking EVC because their CPU hardware does not support the requested EVC mode.  ***Since:*** vSphere API 4.0  Refers instances of *HostSystem*.  | [optional] 
**host_name** | **List[str]** | The names of the hosts in the host array.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.evc_mode_unsupported_by_hosts import EVCModeUnsupportedByHosts

# TODO update the JSON string below
json = "{}"
# create an instance of EVCModeUnsupportedByHosts from a JSON string
evc_mode_unsupported_by_hosts_instance = EVCModeUnsupportedByHosts.from_json(json)
# print the JSON string representation of the object
print EVCModeUnsupportedByHosts.to_json()

# convert the object into a dict
evc_mode_unsupported_by_hosts_dict = evc_mode_unsupported_by_hosts_instance.to_dict()
# create an instance of EVCModeUnsupportedByHosts from a dict
evc_mode_unsupported_by_hosts_form_dict = evc_mode_unsupported_by_hosts.from_dict(evc_mode_unsupported_by_hosts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


