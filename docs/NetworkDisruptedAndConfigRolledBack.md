# NetworkDisruptedAndConfigRolledBack

Thrown if network configuration change disconnected the host from vCenter server and has been rolled back.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The name of host on which the network configuration was rolled back.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.network_disrupted_and_config_rolled_back import NetworkDisruptedAndConfigRolledBack

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkDisruptedAndConfigRolledBack from a JSON string
network_disrupted_and_config_rolled_back_instance = NetworkDisruptedAndConfigRolledBack.from_json(json)
# print the JSON string representation of the object
print NetworkDisruptedAndConfigRolledBack.to_json()

# convert the object into a dict
network_disrupted_and_config_rolled_back_dict = network_disrupted_and_config_rolled_back_instance.to_dict()
# create an instance of NetworkDisruptedAndConfigRolledBack from a dict
network_disrupted_and_config_rolled_back_form_dict = network_disrupted_and_config_rolled_back.from_dict(network_disrupted_and_config_rolled_back_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


