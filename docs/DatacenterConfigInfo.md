# DatacenterConfigInfo

Configuration of the datacenter.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_hardware_version_key** | **str** | Key for Default Hardware Version used on this datacenter in the format of *VirtualMachineConfigOptionDescriptor.key*.  This field affects *VirtualMachineConfigOptionDescriptor.defaultConfigOption* returned by *ComputeResource.environmentBrowser* of all its children with this field unset.  ***Since:*** vSphere API 5.1  | [optional] 
**maximum_hardware_version_key** | **str** | Key for Maximum Hardware Version used on this datacenter in the format of *VirtualMachineConfigOptionDescriptor.key*.  This field affects *VirtualMachineConfigOptionDescriptor.defaultConfigOption* returned by *ComputeResource.environmentBrowser* of all its children with this field unset.  ***Since:*** vSphere API 7.0.2.0  | [optional] 

## Example

```python
from vmware_vi.models.datacenter_config_info import DatacenterConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DatacenterConfigInfo from a JSON string
datacenter_config_info_instance = DatacenterConfigInfo.from_json(json)
# print the JSON string representation of the object
print DatacenterConfigInfo.to_json()

# convert the object into a dict
datacenter_config_info_dict = datacenter_config_info_instance.to_dict()
# create an instance of DatacenterConfigInfo from a dict
datacenter_config_info_form_dict = datacenter_config_info.from_dict(datacenter_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


