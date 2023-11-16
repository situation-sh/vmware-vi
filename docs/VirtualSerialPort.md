# VirtualSerialPort

The <code>*VirtualSerialPort*</code> data object represents a serial port on a virtual machine.  A virtual serial port uses one of the following backing types to specify how the virtual machine performs serial port operations. - Network backing (<code>*VirtualSerialPortURIBackingInfo*</code>)   supports a connection between the virtual machine and a resource   on the network. The virtual machine can initiate a connection with   the network resource, or it can listen for connections originating   from the network. - Pipe backing (<code>*VirtualSerialPortPipeBackingInfo*</code>)   supports I/O through a named pipe. The pipe connects the virtual machine   to a host application or a virtual machine on the same host. - File backing (<code>*VirtualSerialPortFileBackingInfo*</code>)   supports output through the virtual serial port to a file on the same host. - Physical serial port backing   (<code>*VirtualSerialPortDeviceBackingInfo*</code>)   supports a connection between the virtual machine and a   device that is connected to a physical serial port on the host. - ThinPrint backing (<code>*VirtualSerialPortThinPrintBackingInfo*</code>)   provides driver-free printing.    When you use network backing, you can also configure a virtual serial port to use a virtual serial port concentrator. The virtual machine initiates a telnet connection with the concentrator, and the concentrator acts as a proxy between the virtual machine and a system on the network. By using a virtual serial port concentrator, you can maintain the connection between the virtual machine and the network resource when a vMotion event moves the virtual machine from one host to another. Without a virtual serial port concentrator, the connection would be lost. For information about using a serial port concentrator, see _Using a Proxy with vSphere Virtual Serial Ports_.  You can configure a virtual serial port when you create or reconfigure a virtual machine. For example, to create a virtual serial port with network backing, use the following sequence of operations. In this procedure, the virtual serial port uses a proxy and will accept a network connection. 1. Use the <code>*EnvironmentBrowser.QueryConfigOption*</code> method    to determine the backing options that are available on a host.    The method returns a <code>*VirtualMachineConfigOption*</code> data object.    The virtual machine configuration data includes a list of backing options    (<code>*VirtualDeviceOption.backingOption*</code>).    The following pseudocode shows the path to the backing options.            &nbsp;&nbsp;&nbsp;&nbsp;<code>*VirtualMachineConfigOption*.hardwareOptions.VirtualDeviceOption\\[\\].backingOption\\[\\]</code>            The array of virtual device options can include a virtual serial port    (<code>*VirtualSerialPortOption*</code>). The array of serial port    backing options can include URI, file, pipe, or device backing options. 2. Use the <code>*Folder.CreateVM_Task*</code> method    (or the <code>*ResourcePool.CreateChildVM_Task*</code> method)    to create the virtual machine and configure the virtual serial port backing.    Create a <code>*VirtualMachineConfigSpec*</code> data object and nested    data objects for the method's <code>config</code> parameter.    The following pseudocode shows the resulting path to the backing    information.            &nbsp;&nbsp;&nbsp;&nbsp;<code>*VirtualMachineConfigSpec*.deviceChange\\[\\].device.backing</code>            Set the direction property to \"server\" to direct the virtual machine to accept    a connection. Set the serviceURI property to the URI for the host on which    the virtual machine runs.     If you use physical device backing (<code>*VirtualSerialPortDeviceBackingOption*</code>), you should also use the <code>*EnvironmentBrowser.QueryConfigTarget*</code> method to determine if a serial device is available before configuring device backing. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**yield_on_poll** | **bool** | Enables CPU yield behavior.  If you set &lt;code&gt;yieldOnPoll&lt;/code&gt; to &lt;code&gt;true&lt;/code&gt;, the virtual machine will periodically relinquish the processor if its sole task is polling the virtual serial port. The amount of time it takes to regain the processor will depend on the degree of other virtual machine activity on the host.  To use this property, the CPU yield option must be supported. (See the &lt;code&gt;*VirtualSerialPortOption.yieldOnPoll*&lt;/code&gt; property for the virtual serial port option object.)  | 

## Example

```python
from vmware_vi.models.virtual_serial_port import VirtualSerialPort

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSerialPort from a JSON string
virtual_serial_port_instance = VirtualSerialPort.from_json(json)
# print the JSON string representation of the object
print VirtualSerialPort.to_json()

# convert the object into a dict
virtual_serial_port_dict = virtual_serial_port_instance.to_dict()
# create an instance of VirtualSerialPort from a dict
virtual_serial_port_form_dict = virtual_serial_port.from_dict(virtual_serial_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


