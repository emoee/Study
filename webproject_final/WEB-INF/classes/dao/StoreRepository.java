package dao;
import java.util.ArrayList;

import dto.Store;
public class StoreRepository {
	private ArrayList<Store> listOfStores = new ArrayList<>();
	private static StoreRepository instance = new StoreRepository();
	
	public static StoreRepository getInstance() {
		return instance;
	}
	private StoreRepository() {
		
	}
	
	public ArrayList<Store> getAllProducts(){
		return listOfStores;
	}
	
	public void addProduct(Store store) {
		listOfStores.add(store);
	}
	
	public Store getStoreById(String storeId) {
		Store storeById = null;
		for (int i=0; i<listOfStores.size(); i++) {
			Store store = listOfStores.get(i);
			if(store != null && store.getSid() != null && store.getSid().equals(storeId)) {
				storeById = store;
				break;
			}
		}
		return storeById;
	}
}
