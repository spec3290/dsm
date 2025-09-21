function solution(num_list, n) {
    var answer;
    var list1 = [];
    var list2 = [];
    list1 = num_list.slice(n)
    list2 = num_list.slice(0,n)
    answer = list1.concat(list2)
    return answer;
}