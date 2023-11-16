# VirtualDeviceConfigSpec

The VirtualDeviceSpec data object type encapsulates change specifications for an individual virtual device.  The virtual device being added or modified must be fully specified. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**VirtualDeviceConfigSpecOperationEnum**](VirtualDeviceConfigSpecOperationEnum.md) |  | [optional] 
**file_operation** | [**VirtualDeviceConfigSpecFileOperationEnum**](VirtualDeviceConfigSpecFileOperationEnum.md) |  | [optional] 
**device** | [**VirtualDevice**](VirtualDevice.md) |  | 
**profile** | [**List[VirtualMachineProfileSpec]**](VirtualMachineProfileSpec.md) | Virtual Device Profile requirement.  Profiles are solution specifics. Storage Profile Based Management(SPBM) is a vSphere server extension. The API users who want to provision VMs using Storage Profiles, need to interact with SPBM service. This is an optional parameter and if user doesn&#39;t specify profile, the default behavior will apply.  ***Since:*** vSphere API 5.5  | [optional] 
**backing** | [**VirtualDeviceConfigSpecBackingSpec**](VirtualDeviceConfigSpecBackingSpec.md) |  | [optional] 
**filter_spec** | [**List[VirtualMachineBaseIndependentFilterSpec]**](VirtualMachineBaseIndependentFilterSpec.md) | List of independent filters *VirtualMachineIndependentFilterSpec* to configure on the virtual device.  ***Since:*** vSphere API 7.0.2.1  | [optional] 
**change_mode** | **str** | The change mode of the device.  The values of the mode will be one of *VirtualDeviceConfigSpecChangeMode_enum* enumerations. On unset, default to &#39;fail&#39;.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_device_config_spec import VirtualDeviceConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceConfigSpec from a JSON string
virtual_device_config_spec_instance = VirtualDeviceConfigSpec.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceConfigSpec.to_json()

# convert the object into a dict
virtual_device_config_spec_dict = virtual_device_config_spec_instance.to_dict()
# create an instance of VirtualDeviceConfigSpec from a dict
virtual_device_config_spec_form_dict = virtual_device_config_spec.from_dict(virtual_device_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


