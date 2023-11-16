# ArrayOfVirtualSerialPort

A boxed array of *VirtualSerialPort*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualSerialPort]**](VirtualSerialPort.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_serial_port import ArrayOfVirtualSerialPort

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualSerialPort from a JSON string
array_of_virtual_serial_port_instance = ArrayOfVirtualSerialPort.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualSerialPort.to_json()

# convert the object into a dict
array_of_virtual_serial_port_dict = array_of_virtual_serial_port_instance.to_dict()
# create an instance of ArrayOfVirtualSerialPort from a dict
array_of_virtual_serial_port_form_dict = array_of_virtual_serial_port.from_dict(array_of_virtual_serial_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


