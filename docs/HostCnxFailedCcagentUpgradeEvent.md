# HostCnxFailedCcagentUpgradeEvent

This event records a failure to connect to a host due to a conflict with an upgrade or installation of the host agent. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_cnx_failed_ccagent_upgrade_event import HostCnxFailedCcagentUpgradeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostCnxFailedCcagentUpgradeEvent from a JSON string
host_cnx_failed_ccagent_upgrade_event_instance = HostCnxFailedCcagentUpgradeEvent.from_json(json)
# print the JSON string representation of the object
print HostCnxFailedCcagentUpgradeEvent.to_json()

# convert the object into a dict
host_cnx_failed_ccagent_upgrade_event_dict = host_cnx_failed_ccagent_upgrade_event_instance.to_dict()
# create an instance of HostCnxFailedCcagentUpgradeEvent from a dict
host_cnx_failed_ccagent_upgrade_event_form_dict = host_cnx_failed_ccagent_upgrade_event.from_dict(host_cnx_failed_ccagent_upgrade_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


