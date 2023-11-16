# DvsSingleIpPort

This class defines a Single Port  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_number** | **int** | The IP port number.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.dvs_single_ip_port import DvsSingleIpPort

# TODO update the JSON string below
json = "{}"
# create an instance of DvsSingleIpPort from a JSON string
dvs_single_ip_port_instance = DvsSingleIpPort.from_json(json)
# print the JSON string representation of the object
print DvsSingleIpPort.to_json()

# convert the object into a dict
dvs_single_ip_port_dict = dvs_single_ip_port_instance.to_dict()
# create an instance of DvsSingleIpPort from a dict
dvs_single_ip_port_form_dict = dvs_single_ip_port.from_dict(dvs_single_ip_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


