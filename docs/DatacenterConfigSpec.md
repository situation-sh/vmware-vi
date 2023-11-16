# DatacenterConfigSpec

Changes to apply to the datacenter configuration.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_hardware_version_key** | **str** | Key for Default Hardware Version to be used on this datacenter in the format of *VirtualMachineConfigOptionDescriptor.key*.  Setting this field affects *VirtualMachineConfigOptionDescriptor.defaultConfigOption* returned by *ComputeResource.environmentBrowser* of all its children with this field unset.  ***Since:*** vSphere API 5.1  | [optional] 
**maximum_hardware_version_key** | **str** | Key for Maximum Hardware Version to be used on this datacenter in the format of *VirtualMachineConfigOptionDescriptor.key*.  Setting this field affects *VirtualMachineConfigOptionDescriptor.defaultConfigOption* returned by *ComputeResource.environmentBrowser* of all its children with this field unset.  ***Since:*** vSphere API 7.0.2.0  | [optional] 

## Example

```python
from vmware_vi.models.datacenter_config_spec import DatacenterConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DatacenterConfigSpec from a JSON string
datacenter_config_spec_instance = DatacenterConfigSpec.from_json(json)
# print the JSON string representation of the object
print DatacenterConfigSpec.to_json()

# convert the object into a dict
datacenter_config_spec_dict = datacenter_config_spec_instance.to_dict()
# create an instance of DatacenterConfigSpec from a dict
datacenter_config_spec_form_dict = datacenter_config_spec.from_dict(datacenter_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


