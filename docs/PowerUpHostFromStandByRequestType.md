# PowerUpHostFromStandByRequestType

The parameters of *HostSystem.PowerUpHostFromStandBy_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout_sec** | **int** | The task completes when the host successfully exits standby state and sends a heartbeat signal. If nothing is received from the host for timeoutSec seconds, the host is declared timedout, and the task is assumed failed.  | 

## Example

```python
from vmware_vi.models.power_up_host_from_stand_by_request_type import PowerUpHostFromStandByRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of PowerUpHostFromStandByRequestType from a JSON string
power_up_host_from_stand_by_request_type_instance = PowerUpHostFromStandByRequestType.from_json(json)
# print the JSON string representation of the object
print PowerUpHostFromStandByRequestType.to_json()

# convert the object into a dict
power_up_host_from_stand_by_request_type_dict = power_up_host_from_stand_by_request_type_instance.to_dict()
# create an instance of PowerUpHostFromStandByRequestType from a dict
power_up_host_from_stand_by_request_type_form_dict = power_up_host_from_stand_by_request_type.from_dict(power_up_host_from_stand_by_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


