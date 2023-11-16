# VirtualDeviceRemoteDeviceBackingInfo

<code>*VirtualDeviceRemoteDeviceBackingInfo*</code> is a data object type for information about a remote device backing used by a device in a virtual machine.  The primary difference between a remote device backing and a local device backing is that the VirtualCenter server cannot provide a list of remote host devices available for this virtual device backing. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | **str** | The name of the device on the remote system.  | 
**use_auto_detect** | **bool** | Indicates whether the device should be auto detected instead of directly specified.  If this value is set to TRUE, &lt;code&gt;deviceName&lt;/code&gt; is ignored.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.virtual_device_remote_device_backing_info import VirtualDeviceRemoteDeviceBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceRemoteDeviceBackingInfo from a JSON string
virtual_device_remote_device_backing_info_instance = VirtualDeviceRemoteDeviceBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceRemoteDeviceBackingInfo.to_json()

# convert the object into a dict
virtual_device_remote_device_backing_info_dict = virtual_device_remote_device_backing_info_instance.to_dict()
# create an instance of VirtualDeviceRemoteDeviceBackingInfo from a dict
virtual_device_remote_device_backing_info_form_dict = virtual_device_remote_device_backing_info.from_dict(virtual_device_remote_device_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


