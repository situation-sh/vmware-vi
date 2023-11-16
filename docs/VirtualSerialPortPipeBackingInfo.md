# VirtualSerialPortPipeBackingInfo

The <code>*VirtualSerialPortPipeBackingInfo*</code> data object defines information for backing a <code>*VirtualSerialPort*</code> with a named pipe.  You can use a pipe to connect a virtual serial port to a host application or to another virtual machine on the host computer. This is useful for capturing debugging information sent through the virtual serial port. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | Indicates the role the virtual machine assumes as an endpoint for the pipe.  The valid values are \&quot;client\&quot; or \&quot;server\&quot;.  | 
**no_rx_loss** | **bool** | Enables optimized data transfer over the pipe.  When you use this feature, the ESX server buffers data to prevent data overrun. This allows the virtual machine to read all of the data transferred over the pipe with no data loss. To use optimized data transfer, set &lt;code&gt;noRxLoss&lt;/code&gt; to &lt;code&gt;true&lt;/code&gt;. To disable this feature, set the property to &lt;code&gt;false.  This property is optional. If this property is not set, the ESX server uses the default value specified in the pipe backing options (noRxLoss.defaultValue - see &lt;code&gt;*VirtualSerialPortPipeBackingOption.noRxLoss*&lt;/code&gt; in the pipe backing option object).  To use this property, optimized data transfer must be supported on the host. (See &lt;code&gt;*VirtualSerialPortPipeBackingOption.noRxLoss*&lt;/code&gt; in the pipe backing option object.) If the ESX server does not support the option, it ignores the &lt;code&gt;noRxLoss&lt;/code&gt; setting in the pipe backing information object.  **Note**: You can use this feature even if the other end of the pipe is not an application, but this is more likely to fail.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_serial_port_pipe_backing_info import VirtualSerialPortPipeBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSerialPortPipeBackingInfo from a JSON string
virtual_serial_port_pipe_backing_info_instance = VirtualSerialPortPipeBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualSerialPortPipeBackingInfo.to_json()

# convert the object into a dict
virtual_serial_port_pipe_backing_info_dict = virtual_serial_port_pipe_backing_info_instance.to_dict()
# create an instance of VirtualSerialPortPipeBackingInfo from a dict
virtual_serial_port_pipe_backing_info_form_dict = virtual_serial_port_pipe_backing_info.from_dict(virtual_serial_port_pipe_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


