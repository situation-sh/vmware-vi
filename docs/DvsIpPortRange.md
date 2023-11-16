# DvsIpPortRange

This class defines a range of Ports.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_port_number** | **int** | Starting port number of the ports range.  ***Since:*** vSphere API 5.5  | 
**end_port_number** | **int** | Ending port number of the ports range.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.dvs_ip_port_range import DvsIpPortRange

# TODO update the JSON string below
json = "{}"
# create an instance of DvsIpPortRange from a JSON string
dvs_ip_port_range_instance = DvsIpPortRange.from_json(json)
# print the JSON string representation of the object
print DvsIpPortRange.to_json()

# convert the object into a dict
dvs_ip_port_range_dict = dvs_ip_port_range_instance.to_dict()
# create an instance of DvsIpPortRange from a dict
dvs_ip_port_range_form_dict = dvs_ip_port_range.from_dict(dvs_ip_port_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


