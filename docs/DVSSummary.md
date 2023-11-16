# DVSSummary

Summary of the distributed switch configuration.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the switch.  ***Since:*** vSphere API 4.0  | 
**uuid** | **str** | The generated UUID of the switch.  ***Since:*** vSphere API 4.0  | 
**num_ports** | **int** | Current number of ports, not including conflict ports.  ***Since:*** vSphere API 4.0  | 
**product_info** | [**DistributedVirtualSwitchProductSpec**](DistributedVirtualSwitchProductSpec.md) |  | [optional] 
**host_member** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The names of the hosts that join the switch.  ***Since:*** vSphere API 4.0  Refers instances of *HostSystem*.  | [optional] 
**vm** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The Virtual Machines with Virtual NICs that connect to the switch.  In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Since this property is on a DataObject, an update returned by WaitForUpdatesEx may contain values for this property when some other property on the DataObject changes. If this update is a result of a call to WaitForUpdatesEx with a non-empty version parameter, the value for this property may not be current.  ***Since:*** vSphere API 4.0  Refers instances of *VirtualMachine*.  | [optional] 
**host** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The hosts with Virtual NICs that connect to the switch.  ***Since:*** vSphere API 4.0  Refers instances of *HostSystem*.  | [optional] 
**portgroup_name** | **List[str]** | The names of the portgroups that are defined on the switch.  ***Since:*** vSphere API 4.0  | [optional] 
**description** | **str** | A description string of the switch.  ***Since:*** vSphere API 4.0  | [optional] 
**contact** | [**DVSContactInfo**](DVSContactInfo.md) |  | [optional] 
**num_hosts** | **int** | The number of hosts in the switch.  The value of this property is not affected by the privileges granted to the current user.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.dvs_summary import DVSSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DVSSummary from a JSON string
dvs_summary_instance = DVSSummary.from_json(json)
# print the JSON string representation of the object
print DVSSummary.to_json()

# convert the object into a dict
dvs_summary_dict = dvs_summary_instance.to_dict()
# create an instance of DVSSummary from a dict
dvs_summary_form_dict = dvs_summary.from_dict(dvs_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


