# VirtualDeviceDeviceGroupInfo

<code>*VirtualDeviceDeviceGroupInfo*</code> contains information about the device group device is assigned to. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_instance_key** | **int** | Device group instance key from &lt;code&gt;*VirtualMachineVirtualDeviceGroupsDeviceGroup*&lt;/code&gt;.  | 
**sequence_id** | **int** | Device sequence in the group.  Small unique positive integer obtained from &lt;code&gt;*VirtualMachineVendorDeviceGroupInfoComponentDeviceInfo.device*&lt;/code&gt; template.  | 

## Example

```python
from vmware_vi.models.virtual_device_device_group_info import VirtualDeviceDeviceGroupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceDeviceGroupInfo from a JSON string
virtual_device_device_group_info_instance = VirtualDeviceDeviceGroupInfo.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceDeviceGroupInfo.to_json()

# convert the object into a dict
virtual_device_device_group_info_dict = virtual_device_device_group_info_instance.to_dict()
# create an instance of VirtualDeviceDeviceGroupInfo from a dict
virtual_device_device_group_info_form_dict = virtual_device_device_group_info.from_dict(virtual_device_device_group_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


