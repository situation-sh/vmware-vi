# ArrayOfVMwareVspanPort

A boxed array of *VMwareVspanPort*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VMwareVspanPort]**](VMwareVspanPort.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_mware_vspan_port import ArrayOfVMwareVspanPort

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVMwareVspanPort from a JSON string
array_of_v_mware_vspan_port_instance = ArrayOfVMwareVspanPort.from_json(json)
# print the JSON string representation of the object
print ArrayOfVMwareVspanPort.to_json()

# convert the object into a dict
array_of_v_mware_vspan_port_dict = array_of_v_mware_vspan_port_instance.to_dict()
# create an instance of ArrayOfVMwareVspanPort from a dict
array_of_v_mware_vspan_port_form_dict = array_of_v_mware_vspan_port.from_dict(array_of_v_mware_vspan_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


