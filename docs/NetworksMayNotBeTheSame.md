# NetworksMayNotBeTheSame

Used as a warning if a virtual machine provisioning operation is done across datacenters.  This warns that the network used by the virtual machine before and after the operation may not be the same even though the two networks have the same name. This is because network names are only unique within a datacenter.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the network.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.networks_may_not_be_the_same import NetworksMayNotBeTheSame

# TODO update the JSON string below
json = "{}"
# create an instance of NetworksMayNotBeTheSame from a JSON string
networks_may_not_be_the_same_instance = NetworksMayNotBeTheSame.from_json(json)
# print the JSON string representation of the object
print NetworksMayNotBeTheSame.to_json()

# convert the object into a dict
networks_may_not_be_the_same_dict = networks_may_not_be_the_same_instance.to_dict()
# create an instance of NetworksMayNotBeTheSame from a dict
networks_may_not_be_the_same_form_dict = networks_may_not_be_the_same.from_dict(networks_may_not_be_the_same_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


