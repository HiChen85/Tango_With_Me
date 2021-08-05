$(document).ready(function(){
    $("#index_search").click(function(){
        var search_item = $("#search").val().trim()
        $.ajax({
            url:'search/search/',
            type:'POST',
            data:{search_item:search_item},
            success:function(data){
                alert(data)
            },
            fail:function(data){
                alert("fail")
            }
        })
    })
})