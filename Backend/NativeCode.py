potenciaNative = '''function potenciaNativas(num::Int64,power::Int64)::Int64
    answer = 1;
    if (num > 0) && (power==0)
        return answer;
    elseif (num == 0) && (power>=1)
        return 0;
    else
        for i in 1:power
            answer = answer*num;
        end;
        return answer;
    end;
end;

function potenciaStringNativas(dato::String,power::Int64)::String
        answer = "";
        for i in 1:power
            answer = answer*num;
        end;
        return answer;
end;
'''