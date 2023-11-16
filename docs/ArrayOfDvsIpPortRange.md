# ArrayOfDvsIpPortRange

A boxed array of *DvsIpPortRange*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsIpPortRange]**](DvsIpPortRange.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_ip_port_range import ArrayOfDvsIpPortRange

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsIpPortRange from a JSON string
array_of_dvs_ip_port_range_instance = ArrayOfDvsIpPortRange.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsIpPortRange.to_json()

# convert the object into a dict
array_of_dvs_ip_port_range_dict = array_of_dvs_ip_port_range_instance.to_dict()
# create an instance of ArrayOfDvsIpPortRange from a dict
array_of_dvs_ip_port_range_form_dict = array_of_dvs_ip_port_range.from_dict(array_of_dvs_ip_port_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


