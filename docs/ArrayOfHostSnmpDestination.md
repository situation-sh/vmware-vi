# ArrayOfHostSnmpDestination

A boxed array of *HostSnmpDestination*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSnmpDestination]**](HostSnmpDestination.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_snmp_destination import ArrayOfHostSnmpDestination

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSnmpDestination from a JSON string
array_of_host_snmp_destination_instance = ArrayOfHostSnmpDestination.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSnmpDestination.to_json()

# convert the object into a dict
array_of_host_snmp_destination_dict = array_of_host_snmp_destination_instance.to_dict()
# create an instance of ArrayOfHostSnmpDestination from a dict
array_of_host_snmp_destination_form_dict = array_of_host_snmp_destination.from_dict(array_of_host_snmp_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


