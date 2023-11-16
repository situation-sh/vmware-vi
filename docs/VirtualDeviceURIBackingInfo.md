# VirtualDeviceURIBackingInfo

The <code>*VirtualDeviceURIBackingInfo*</code> data object type defines information for using a network socket as backing for a virtual device.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_uri** | **str** | Identifies the local host or a system on the network, depending on the value of &lt;code&gt;*VirtualDeviceURIBackingInfo.direction*&lt;/code&gt;. - If you use the virtual machine as a server, the URI identifies   the host on which the virtual machine runs. In this case,   the host name part of the URI should be empty, or it should   specify the address of the local host. - If you use the virtual machine as a client, the URI identifies   the remote system on the network.    ***Since:*** vSphere API 4.1  | 
**direction** | **str** | The direction of the connection.  For possible values see *VirtualDeviceURIBackingOptionDirection_enum*  ***Since:*** vSphere API 4.1  | 
**proxy_uri** | **str** | Identifies a proxy service that provides network access to the &lt;code&gt;*VirtualDeviceURIBackingInfo.serviceURI*&lt;/code&gt;.  If you specify a proxy URI, the virtual machine initiates a connection with the proxy service and forwards the *VirtualDeviceURIBackingInfo.serviceURI* and *VirtualDeviceURIBackingInfo.direction* to the proxy.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.virtual_device_uri_backing_info import VirtualDeviceURIBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceURIBackingInfo from a JSON string
virtual_device_uri_backing_info_instance = VirtualDeviceURIBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceURIBackingInfo.to_json()

# convert the object into a dict
virtual_device_uri_backing_info_dict = virtual_device_uri_backing_info_instance.to_dict()
# create an instance of VirtualDeviceURIBackingInfo from a dict
virtual_device_uri_backing_info_form_dict = virtual_device_uri_backing_info.from_dict(virtual_device_uri_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


