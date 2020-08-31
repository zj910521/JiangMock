    $("#add_api").click(function () {
        console.log("1234");
        $.get("/getProjectInfo", function (data) {
            var data = JSON.parse(data);
            $("#api_pro_name").empty();
            op = "";
            for (var i = 0; i < data.length; i++) {
                op += "<option " + "'pro_id'=" + data[i].pro_id + ">" + data[i].pro_name + "</option>";
            }
            console.log(op);
            $("#api_pro_name").append(op);
        });
    });

    $("#save_pro").click(function () {
        console.log("save_pro");
        var pro_name = $("#project_name").val();
        var pro_desc = $("#project_desc").val();
        $.ajax({
            type: "POST",
            url: "/project/1",
            data: {pro_name: pro_name, pro_desc: pro_desc},
            dataType: "json",
            success: function (data) {
                console.log(data);
                $("#project_name").empty();
                $("#project_desc").empty();
                swal({
                    title: "添加成功",
                    type: "success",
                    confirmButtonText: "确定",
                    closeOnConfirm: false
                });
                $("#myModal > div > div > div.modal-footer > button.btn.btn-default").click()
                setTimeout(function () {
                    window.location.reload();
                }, 500);
            }
        });
    });

    $("#save_api").click(function () {
        var api_pro_name = $("#api_pro_name").val();
        var api_method = $("#api_method").val();
        var api_name = $("#api_name").val();
        var api_url = $("#api_url").val();
        console.log(api_pro_name,api_method,api_name,api_url);
        $.ajax({
            type: "POST",
            url: "/api/1",
            data: {api_pro_name: api_pro_name, api_method: api_method,api_name:api_name,api_url:api_url},
            dataType: "json",
            success: function (data) {
                console.log(data);
                $("#api_name").empty();
                $("#api_url").empty();
                swal({
                    title: "添加成功",
                    type: "success",
                    confirmButtonText: "确定",
                    closeOnConfirm: false
                });
                $("#myModal > div > div > div.modal-footer > button.btn.btn-default").click();
                setTimeout(function () {
                    window.location.reload();
                }, 500);
            }
        });
    });