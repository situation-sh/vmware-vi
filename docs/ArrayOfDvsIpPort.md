# ArrayOfDvsIpPort

A boxed array of *DvsIpPort*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsIpPort]**](DvsIpPort.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_ip_port import ArrayOfDvsIpPort

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsIpPort from a JSON string
array_of_dvs_ip_port_instance = ArrayOfDvsIpPort.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsIpPort.to_json()

# convert the object into a dict
array_of_dvs_ip_port_dict = array_of_dvs_ip_port_instance.to_dict()
# create an instance of ArrayOfDvsIpPort from a dict
array_of_dvs_ip_port_form_dict = array_of_dvs_ip_port.from_dict(array_of_dvs_ip_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


