# DisconnectedHostsBlockingEVC

An attempt to enable Enhanced VMotion Compatibility on a cluster, or to select a less-featureful EVC mode for a cluster where EVC is already enabled, has failed because the cluster contains one or more disconnected hosts.  ***Since:*** VI API 2.5u2 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.disconnected_hosts_blocking_evc import DisconnectedHostsBlockingEVC

# TODO update the JSON string below
json = "{}"
# create an instance of DisconnectedHostsBlockingEVC from a JSON string
disconnected_hosts_blocking_evc_instance = DisconnectedHostsBlockingEVC.from_json(json)
# print the JSON string representation of the object
print DisconnectedHostsBlockingEVC.to_json()

# convert the object into a dict
disconnected_hosts_blocking_evc_dict = disconnected_hosts_blocking_evc_instance.to_dict()
# create an instance of DisconnectedHostsBlockingEVC from a dict
disconnected_hosts_blocking_evc_form_dict = disconnected_hosts_blocking_evc.from_dict(disconnected_hosts_blocking_evc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


