# VirtualAppSummary

This data object type encapsulates a typical set of resource pool information that is useful for list views and summary pages.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**VAppProductInfo**](VAppProductInfo.md) |  | [optional] 
**v_app_state** | [**VirtualAppVAppStateEnum**](VirtualAppVAppStateEnum.md) |  | [optional] 
**suspended** | **bool** | Whether a vApp is suspended, in the process of being suspended, or in the process of being resumed.  A stopped vApp is marked as suspended under the following conditions: - All child virtual machines are either suspended or powered-off. - There is at least one suspended virtual machine for which the   stop action is not \&quot;suspend\&quot;.    If the vAppState property is \&quot;stopped\&quot;, the value is set to true if the vApp is suspended (according the the above definition).  If the vAppState property is \&quot;stopping\&quot; or \&quot;starting\&quot; and the suspend flag is set to true, then the vApp is either in the process of being suspended or resumed from a suspended state, respectively.  If the vAppState property is \&quot;started\&quot;, then the suspend flag is set to false.  ***Since:*** vSphere API 4.1  | [optional] 
**install_boot_required** | **bool** | Whether one or more VMs in this vApp require a reboot to finish installation.  ***Since:*** vSphere API 4.0  | [optional] 
**instance_uuid** | **str** | vCenter-specific UUID of the vApp  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.virtual_app_summary import VirtualAppSummary

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAppSummary from a JSON string
virtual_app_summary_instance = VirtualAppSummary.from_json(json)
# print the JSON string representation of the object
print VirtualAppSummary.to_json()

# convert the object into a dict
virtual_app_summary_dict = virtual_app_summary_instance.to_dict()
# create an instance of VirtualAppSummary from a dict
virtual_app_summary_form_dict = virtual_app_summary.from_dict(virtual_app_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


