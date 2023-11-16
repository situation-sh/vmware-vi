# DvsIpPort

Base class for specifying Ports.  Objects of the base class represent any port (single/range/list).  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.dvs_ip_port import DvsIpPort

# TODO update the JSON string below
json = "{}"
# create an instance of DvsIpPort from a JSON string
dvs_ip_port_instance = DvsIpPort.from_json(json)
# print the JSON string representation of the object
print DvsIpPort.to_json()

# convert the object into a dict
dvs_ip_port_dict = dvs_ip_port_instance.to_dict()
# create an instance of DvsIpPort from a dict
dvs_ip_port_form_dict = dvs_ip_port.from_dict(dvs_ip_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


