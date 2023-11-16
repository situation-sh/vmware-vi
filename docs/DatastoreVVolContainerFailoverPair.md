# DatastoreVVolContainerFailoverPair

A pair of source and target VVol containers and mapping of VVol IDs from source to target.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src_container** | **str** | Storage container on the source side.  ***Since:*** vSphere API 6.5  | [optional] 
**tgt_container** | **str** | Storage container on the target side.  ***Since:*** vSphere API 6.5  | 
**vvol_mapping** | [**List[KeyValue]**](KeyValue.md) | Mapping of VVol IDs from source to target corresponding to the given set of containers.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.datastore_v_vol_container_failover_pair import DatastoreVVolContainerFailoverPair

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreVVolContainerFailoverPair from a JSON string
datastore_v_vol_container_failover_pair_instance = DatastoreVVolContainerFailoverPair.from_json(json)
# print the JSON string representation of the object
print DatastoreVVolContainerFailoverPair.to_json()

# convert the object into a dict
datastore_v_vol_container_failover_pair_dict = datastore_v_vol_container_failover_pair_instance.to_dict()
# create an instance of DatastoreVVolContainerFailoverPair from a dict
datastore_v_vol_container_failover_pair_form_dict = datastore_v_vol_container_failover_pair.from_dict(datastore_v_vol_container_failover_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


