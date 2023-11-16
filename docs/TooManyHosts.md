# TooManyHosts

Thrown when a computer resource does not accept any more hosts.  Clusters with DRS or HA enabled might impose a limit on the size of the cluster. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.too_many_hosts import TooManyHosts

# TODO update the JSON string below
json = "{}"
# create an instance of TooManyHosts from a JSON string
too_many_hosts_instance = TooManyHosts.from_json(json)
# print the JSON string representation of the object
print TooManyHosts.to_json()

# convert the object into a dict
too_many_hosts_dict = too_many_hosts_instance.to_dict()
# create an instance of TooManyHosts from a dict
too_many_hosts_form_dict = too_many_hosts.from_dict(too_many_hosts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


