# HeterogenousHostsBlockingEVC

An attempt to enable Enhanced VMotion Compatibility on a cluster has failed because the cluster contains CPUs from more than one vendor.  ***Since:*** VI API 2.5u2 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.heterogenous_hosts_blocking_evc import HeterogenousHostsBlockingEVC

# TODO update the JSON string below
json = "{}"
# create an instance of HeterogenousHostsBlockingEVC from a JSON string
heterogenous_hosts_blocking_evc_instance = HeterogenousHostsBlockingEVC.from_json(json)
# print the JSON string representation of the object
print HeterogenousHostsBlockingEVC.to_json()

# convert the object into a dict
heterogenous_hosts_blocking_evc_dict = heterogenous_hosts_blocking_evc_instance.to_dict()
# create an instance of HeterogenousHostsBlockingEVC from a dict
heterogenous_hosts_blocking_evc_form_dict = heterogenous_hosts_blocking_evc.from_dict(heterogenous_hosts_blocking_evc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


