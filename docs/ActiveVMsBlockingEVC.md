# ActiveVMsBlockingEVC

An attempt to enable Enhanced VMotion Compatibility on a cluster, or to select a less-featureful EVC mode for a cluster where EVC is already enabled, has failed for the following reason: - The cluster contains hosts that expose additional compatibility-   relevant CPU features beyond those present in the baseline of the   requested EVC mode. - Those hosts have powered-on or suspended virtual machines.    Therefore the EVC configuration has been rejected since it may suppress CPU features that are currently in-use.  ***Since:*** VI API 2.5u2 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evc_mode** | **str** | The requested EVC mode.  ***Since:*** vSphere API 4.0  | [optional] 
**host** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Hosts with active virtual machines that are blocking the operation, because the hosts expose compatibility-relevant CPU features not present in the baseline of the requested EVC mode.  Note that in rare cases, a host may be on this list even if its *maxEVCModeKey* corresponds to the requested EVC mode. This means that even though that EVC mode is the best match for the host&#39;s hardware, the host still has some features beyond those present in the baseline for that EVC mode.  ***Since:*** vSphere API 4.0  Refers instances of *HostSystem*.  | [optional] 
**host_name** | **List[str]** | The names of the hosts in the host array.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.active_vms_blocking_evc import ActiveVMsBlockingEVC

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveVMsBlockingEVC from a JSON string
active_vms_blocking_evc_instance = ActiveVMsBlockingEVC.from_json(json)
# print the JSON string representation of the object
print ActiveVMsBlockingEVC.to_json()

# convert the object into a dict
active_vms_blocking_evc_dict = active_vms_blocking_evc_instance.to_dict()
# create an instance of ActiveVMsBlockingEVC from a dict
active_vms_blocking_evc_form_dict = active_vms_blocking_evc.from_dict(active_vms_blocking_evc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


