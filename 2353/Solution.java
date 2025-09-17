import java.util.*;

class FoodRatings {
    Map<String, Food> nameFoods;
    Map<String, PriorityQueue<Food>> cuisinesFoods;
    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        nameFoods = new HashMap<>();
        cuisinesFoods = new HashMap<>();
        for(int i = 0; i < foods.length; i++) {
            Food cur = new Food(foods[i], ratings[i], cuisines[i]);
            nameFoods.put(foods[i], cur);
            if(!cuisinesFoods.containsKey(cuisines[i])) {
                cuisinesFoods.put(cuisines[i], new PriorityQueue<>(Comparator
                                .comparing((Food f) -> -f.rating)
                                .thenComparing((Food f) -> f.name)
                        )
                );
            }
            cuisinesFoods.get(cuisines[i]).offer(cur);

        }
    }

    public void changeRating(String food, int newRating) {
        Food f  = nameFoods.get(food);
        f.removed = true;
        String cuisine = f.cuisine;
        nameFoods.remove(food);
        Food newFood = new Food(food, newRating, cuisine);
        nameFoods.put(food, newFood);
        cuisinesFoods.get(cuisine).offer(newFood);
    }

    public String highestRated(String cuisine) {
        PriorityQueue<Food> pq = cuisinesFoods.get(cuisine);
        while(!pq.isEmpty() && pq.peek().removed){
            pq.poll();
        }
        System.out.println(pq.peek().name + " " + pq.peek().rating);
        return pq.peek().name;
    }
}
class Food {
    String name;
    int rating;
    String cuisine;
    boolean removed = false;
    Food(String name, int rating, String cuisine) {
        this.name = name;
        this.rating  = rating;
        this.cuisine = cuisine;
    }
}